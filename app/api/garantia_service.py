# -*- coding: utf-8 -*-

from . import models, garantia_checker_constants
import os
from worker.tasks import fogar_alta_garantia_prestamo, fogar_actualizacion_garantia_prestamo
from django.db import transaction
import logging
from kombu import Connection
from kombu.exceptions import OperationalError
import json

logger = logging.getLogger(__name__)


def operacion_detalle_created_at_fogar(id_garantizar):
    return models.GarantizarFogar.objects.filter(id_garantizar=id_garantizar).exists()


def existe_operacion_detalle(id_garantizar):
    return models.OperacionDetalle.objects.filter(id_garantizar=id_garantizar).exists()


def check_broker_connection():
    try:
        conn = Connection(os.environ['CELERY_BROKER'])
        conn.ensure_connection(max_retries=2, interval_start=0, interval_step=0.1)
    except OperationalError:
        raise RuntimeError("Failed to connect to RabbitMQ instance at {}".format(os.environ['CELERY_BROKER']))


def post_encolar_garantias(garantias_dict):
    url = garantias_dict[garantia_checker_constants.clave_url]
    garantias = garantias_dict[garantia_checker_constants.clave_garantias]
    operacion = models.Operacion.objects.create(total_operaciones=len(garantias),
                                                url_respuesta=url,
                                                representacion_json=json.dumps(garantias_dict, ensure_ascii=False))

    # Valores iniciales
    encolados = []
    no_encolados = []
    sin_procesar = []

    for garantia in garantias:
        id_garantizar = garantia[garantia_checker_constants.clave_garantizar]
        try:
            # Verifico la conexion
            check_broker_connection()
            if not operacion_detalle_created_at_fogar(id_garantizar):
                # Encolo tarea al buffer de entrada
                fogar_alta_garantia_prestamo.s(operacion.pk, garantia).delay()
                # Creo o actualizo una operacion detalle
                registrar_detalle(garantia, id_garantizar, operacion)
                # Guardo id_garantizar para informar al cliente (encoladas)
                encolados.append(id_garantizar)
            else:
                # Guardo id_garantizar para informar al cliente (repetidas)
                no_encolados.append(id_garantizar)
        except Exception as e:
            logger.info(e)
            models.OperacionEncoladaError.objects.create(operacion=operacion,
                                                         id_garantizar=id_garantizar,
                                                         trace=e,
                                                         representacion_json=json.dumps(garantia, ensure_ascii=False))
            # Guardo id_garantizar para informar al cliente (no encoladas)
            sin_procesar.append(id_garantizar)

    # total_encoladas_por_procesar se utilizará para descontar las operaciones pendientes hasta llegar a cero
    actualizar_operacion(encolados, no_encolados, operacion, sin_procesar)

    # Genero respuesta al cliente que invoco el WS
    return {'id_transaccion': operacion.pk, 
        'total_operaciones_recibidas': len(garantias),
        'ids_garantizar_encolados': encolados,
        'ids_garantizar_no_encolados': no_encolados,
        'ids_garantizar_sin_procesar' : sin_procesar}


@transaction.atomic
def actualizar_operacion(encolados, no_encolados, operacion, sin_procesar):
    operacion.update(total_encoladas=len(encolados),
                     total_encoladas_por_procesar=len(encolados),
                     total_no_encoladas=len(sin_procesar),
                     total_registro_previo=len(no_encolados))


@transaction.atomic
def registrar_detalle(garantia, id_garantizar, operacion):
    if not existe_operacion_detalle(id_garantizar):
        models.OperacionDetalle.objects.create(id_garantizar=id_garantizar,
                                               operacion=operacion,
                                               procesado=False,
                                               representacion_json=json.dumps(garantia, ensure_ascii=False))
    else:
        operacion_detalle = models.OperacionDetalle.objects.get(id_garantizar=id_garantizar)
        operacion_detalle.update(
            representacion_json=json.dumps(garantia, ensure_ascii=False),
            procesado=False,
            operacion=operacion)


def put_encolar_garantias(garantias_dict):
    url = garantias_dict[garantia_checker_constants.clave_url]
    garantias = garantias_dict[garantia_checker_constants.clave_garantias]
    operacion = models.Operacion.objects.create(total_operaciones=len(garantias),
                                                url_respuesta=url,
                                                tipo_operacion='ACTUALIZACION',
                                                representacion_json=json.dumps(garantias_dict, ensure_ascii=False))

    # Valores iniciales
    encolados = []
    no_encolados = []
    sin_procesar = []

    for garantia in garantias:
        id_garantizar = garantia[garantia_checker_constants.clave_garantizar]
        try:
            # Verifico la conexion
            check_broker_connection()
            # Encolo tarea al buffer de entrada
            identifier = models.OperacionDetalleHistorial.objects.count()
            fogar_actualizacion_garantia_prestamo.s(operacion.pk, garantia, identifier).delay()
            # Creo objeto OperacionDetalleHistorial
            create_historial_detalle(garantia, id_garantizar, identifier, operacion)
            # Guardo id_garantizar para informar al cliente (encoladas)
            encolados.append(id_garantizar)
        except Exception as e:
            logger.info(e)
            models.OperacionEncoladaError.objects.create(operacion=operacion,
                                                         id_garantizar=id_garantizar,
                                                         trace=e,
                                                         representacion_json=json.dumps(garantia, ensure_ascii=False))
            # Guardo id_garantizar para informar al cliente (no encoladas)
            sin_procesar.append(id_garantizar)

    # total_encoladas_por_procesar se utilizará para descontar las operaciones pendientes hasta llegar a cero
    actualizar_operacion(encolados, no_encolados, operacion, sin_procesar)

    # Genero respuesta al cliente que invoco el WS
    return {'id_transaccion': operacion.pk,
        'total_operaciones_recibidas': len(garantias),
        'ids_garantizar_encolados': encolados,
        'ids_garantizar_no_encolados': no_encolados,
        'ids_garantizar_sin_procesar' : sin_procesar}


@transaction.atomic
def create_historial_detalle(garantia, id_garantizar, identifier, operacion):
    operacion_detalle = models.OperacionDetalle.objects.get(id_garantizar=id_garantizar)
    models.OperacionDetalleHistorial.objects.create(operacion=operacion,
                                                    operacionDetalle=operacion_detalle,
                                                    identifier=identifier,
                                                    representacion_json=json.dumps(garantia, ensure_ascii=False))


@transaction.atomic
def registro_resultado_alta_fogar(id_garantizar, resultado_enviado_fogar, response_fogar, status_code):
    operacionDetalle = models.OperacionDetalle.objects.get(id_garantizar=id_garantizar)
    response_fogar['status_code'] = status_code
    operacionDetalle.update(resultado_fogar_json=json.dumps(response_fogar, ensure_ascii=False),
                            resultado_fogar_raw=response_fogar,
                            procesado=resultado_enviado_fogar,
                            status_code=status_code)

    operacion = operacionDetalle.operacion
    operacion.total_encoladas_por_procesar -= 1
    if resultado_enviado_fogar and response_fogar[garantia_checker_constants.clave_fogar]:
        id_fogar = response_fogar[garantia_checker_constants.clave_fogar]
        models.GarantizarFogar.objects.create(id_garantizar=id_garantizar,
                                              id_fogar=id_fogar)
    operacion.save()
    return operacion


@transaction.atomic
def update_operacion_detalle_by_id_identifier(identifier, resultado_enviado_fogar, response_fogar, status_code):
    operacionDetalleHistorial = models.OperacionDetalleHistorial.objects.get(identifier=identifier)
    response_fogar['status_code'] = status_code
    operacionDetalleHistorial.update(resultado_fogar_json=json.dumps(response_fogar, ensure_ascii=False),
                                     resultado_fogar_raw=response_fogar,
                                     procesado=resultado_enviado_fogar)

    operacion = operacionDetalleHistorial.operacion
    operacion.total_encoladas_por_procesar -= 1
    operacion.save()
    return operacion


@transaction.atomic
def generar_respuesta_garantizar(id_transaccion):
    operacion_entrada = models.Operacion.objects.get(id=id_transaccion)
    resultados = models.OperacionDetalle.objects.filter(operacion=operacion_entrada)

    data = {
        'id_transaccion': id_transaccion,
        'operaciones': [eval(operacion.resultado_fogar_raw) for operacion in resultados],
    }
    operacion_entrada.update(resultado_generado_garantizar_json=json.dumps(data, ensure_ascii=False))
    return data, operacion_entrada


@transaction.atomic
def update_operacion_by_id_transaccion(id_transaccion, resultado_enviado_garantizar, respuesta_garantizar):
    operacion_entrada = models.Operacion.objects.get(pk=id_transaccion)
    operacion_entrada.update(resultado_enviado_garantizar=resultado_enviado_garantizar,
                             respuesta_garantizar_json=json.dumps(respuesta_garantizar, ensure_ascii=False))


@transaction.atomic
def update_operacion(operacion_entrada, resultado_enviado_garantizar, respuesta_garantizar):
    operacion_entrada.update(resultado_enviado_garantizar=resultado_enviado_garantizar,
                             respuesta_garantizar_json=json.dumps(respuesta_garantizar, ensure_ascii=False))
