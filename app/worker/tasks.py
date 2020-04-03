# -*- coding: utf-8 -*-

import logging
import requests
from .worker import app
from api import garantia_service, garantia_checker_constants
from celery.exceptions import MaxRetriesExceededError
from requests.exceptions import ConnectionError
import os
import json

logger = logging.getLogger(__name__)

"""
Cuando total_encoladas_por_procesar == 0, deberia encolar una task en el buffer de salida con id_transaccion
De esta forma, cuando el worker ejecute garantizar_reporte_garantias_procesadas tendria que:
    * Traer de la base todos los OperacionDetalle cuyo Detalle.id sea == id_transaccion
    * Recorrer el resultado para generar el response al WS de garantizar (a.k.a garantizar_mock)
    * Si el request generado termina con OK, actualizo Operacion con retornado_garantizar=True
"""
@app.task(bind=True, 
    name='fogar_alta_garantia_prestamo', 
    default_retry_delay=30,
    max_retries=5, 
    queue='buffer_entrada') 
def fogar_alta_garantia_prestamo(self, id_transaccion, garantia):
    url = os.environ['URL_FOGAR_ALTA']
    try:
        garantia_str = json.dumps(garantia, separators=(',', ':'))
        return post_a_fogar(garantia, garantia_str, url)
    except Exception:
        try:
            self.retry()
            # TODO: podría crear un OperacionEncoladaError para mejorar la auditoría de estos casos, con el trace...
        except MaxRetriesExceededError as e:
            garantia_service.registro_resultado_alta_fogar(garantia[garantia_checker_constants.clave_garantizar],
                                                           False,
                                                           str(e),
                                                           garantia_checker_constants.max_retries_exceeded_status_code)
            return str(e)


def post_a_fogar(garantia, garantia_str, url):
    headers = {'Content-type': 'application/json'}
    response_fogar = requests.post(url, data=garantia_str, headers=headers)
    if status_code_admitido(response_fogar.status_code):
        operacion = garantia_service.registro_resultado_alta_fogar(garantia[garantia_checker_constants.clave_garantizar],
                                                                   True,
                                                                   response_fogar.json(),
                                                                   response_fogar.status_code)
        if operacion.total_encoladas_por_procesar == 0:
            garantizar_reporte_garantias_procesadas.delay(operacion.pk)
        return response_fogar.json()
    else:
        msg = "Status Code inválido: " + str(response_fogar.status_code)
        garantia_service.registro_resultado_alta_fogar(garantia[garantia_checker_constants.clave_garantizar],
                                                       False,
                                                       msg,
                                                       response_fogar.status_code)
        return msg


@app.task(bind=True, 
    name='fogar_actualizacion_garantia_prestamo', 
    default_retry_delay=30,
    max_retries=5,
    queue='buffer_entrada') 
def fogar_actualizacion_garantia_prestamo(self, id_transaccion, garantia, identifier):
    url = os.environ['URL_FOGAR_ACTUALIZACION']
    try:
        garantia_str = json.dumps(garantia, separators=(',', ':'))
        return put_a_fogar(garantia_str, identifier, url)
    except Exception:
        try:
            self.retry()
            # TODO: podría crear un OperacionEncoladaError para mejorar la auditoría de estos casos, con el trace...
        except MaxRetriesExceededError as e:
            garantia_service.update_operacion_detalle_by_id_identifier(identifier,
                                                                       False,
                                                                       str(e),
                                                                       garantia_checker_constants.max_retries_exceeded_status_code)
            return str(e)


def put_a_fogar(garantia_str, identifier, url):
    headers = {'Content-type': 'application/json'}
    #TODO: POST A PUT (coordinar cambio con fogar)
    response_fogar = requests.post(url, data=garantia_str, headers=headers)
    if status_code_admitido(response_fogar.status_code):
        logger.info(response_fogar.json())
        operacion = garantia_service.update_operacion_detalle_by_id_identifier(identifier,
                                                                               True,
                                                                               response_fogar.json(),
                                                                               response_fogar.status_code)
        if operacion.total_encoladas_por_procesar == 0:
            garantizar_reporte_garantias_procesadas.delay(operacion.pk)
        return response_fogar.json()
    else:
        msg = "Status Code inválido: " + str(response_fogar.status_code)
        garantia_service.update_operacion_detalle_by_id_identifier(identifier,
                                                                   False,
                                                                   msg,
                                                                   response_fogar.status_code)
        return msg


@app.task(bind=True, 
    name='garantizar_reporte_garantias_procesadas', 
    default_retry_delay=30,
    max_retries=5,
    queue='buffer_salida') 
def garantizar_reporte_garantias_procesadas(self, id_transaccion):
    try:
        data, operacion_entrada = garantia_service.generar_respuesta_garantizar(id_transaccion)
        return post_to_garantizar(data, id_transaccion, operacion_entrada)

    except ConnectionError:
        try:
            self.retry()
            # TODO: podría crear un OperacionEncoladaError (¿u otra entidad?) para mejorar la auditoría de estos casos, con el trace...
        except MaxRetriesExceededError as e:
            garantia_service.update_operacion_by_id_transaccion(id_transaccion,
                                                                False,
                                                                e)
            return str(e)


def post_to_garantizar(data, id_transaccion, operacion_entrada):
    data_str = json.dumps(data, separators=(',', ':'))
    headers = {'Content-type': 'application/json'}
    r = requests.post(operacion_entrada.url_respuesta, data=data_str, headers=headers)
    if r.ok:
        garantia_service.update_operacion(operacion_entrada,
                                          True,
                                          r.json())
        logger.info(r.json())
        return r.json()
    else:
        msg = str(r.content) + " con status code: " + str(r.status_code)
        logger.info(msg)
        garantia_service.update_operacion_by_id_transaccion(id_transaccion,
                                                            False,
                                                            msg)
        return msg


def status_code_admitido (status_code):
    return status_code == garantia_checker_constants.created_status_code or status_code == garantia_checker_constants.conflict_status_code
