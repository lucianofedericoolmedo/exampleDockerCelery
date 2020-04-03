# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# from django_mysql.models import JSONField
# NOTA: usar JSONField + django_mysql?


### https://stackoverflow.com/questions/12381756/django-calling-update-on-a-single-model-instance-retrieved-by-get
class UpdateMixin(object):
    def update(self, **kwargs):
        if self._state.adding:
            raise self.DoesNotExist
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save(update_fields=kwargs.keys())


class Operacion(models.Model, UpdateMixin):
    API_CHOICES = (
        ('ALTA', 'alta'),
        ('ACTUALIZACION', 'actualizacion'),
    )

    tipo_operacion = models.CharField(max_length=15, choices=API_CHOICES, default='ALTA')
    total_operaciones = models.PositiveIntegerField(blank=False, null=False, default=0)
    total_encoladas = models.PositiveIntegerField(blank=False, null=True, default=0)
    total_no_encoladas = models.PositiveIntegerField(blank=False, null=True, default=0)
    total_encoladas_por_procesar = models.PositiveIntegerField(blank=False, null=True, default=0)
    total_registro_previo = models.PositiveIntegerField(blank=False, null=True, default=0)
    resultado_enviado_garantizar = models.BooleanField(blank=False, null=False, default=False)
    # TODO: Analizar conveniencia de usar jsonfields
    resultado_generado_garantizar_json = models.TextField(blank=True)
    respuesta_garantizar_json = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    url_respuesta = models.TextField(blank=True)
    # TODO: Analizar conveniencia de usar jsonfields
    representacion_json = models.TextField(blank=True)

    def __str__( self ):
        return "Operacion con id de Transaccion {0} con url_respuesta: {1} ".format(self.pk, self.url_respuesta)

    class Meta(object):
        verbose_name_plural = 'Operaciones'
        app_label = 'api'


class OperacionDetalle(models.Model, UpdateMixin):
    id_garantizar = models.CharField(max_length=100, unique=True, null=True, db_index=True)
    procesado = models.BooleanField(blank=False, null=False, default=False)
    operacion = models.ForeignKey(Operacion, blank=False, null=False, on_delete=models.CASCADE)
    resultado_fogar_raw = models.TextField(blank=True)
    # TODO: Analizar conveniencia de usar jsonfields
    resultado_fogar_json = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    status_code = models.CharField(max_length=3, blank=True)
    # TODO: Analizar conveniencia de usar jsonfields
    representacion_json = models.TextField(blank=True)

    def __str__( self ):
        return "Operacion detalle para id de Garantizar {0} ".format( self.id_garantizar )

    class Meta:
        indexes = [models.Index(fields=['id_garantizar', ]), ]
        app_label = 'api'


class OperacionDetalleHistorial(models.Model, UpdateMixin):
    operacion = models.ForeignKey(Operacion, blank=False, null=False, on_delete=models.CASCADE)
    operacionDetalle = models.ForeignKey(OperacionDetalle, blank=False, null=False, on_delete=models.CASCADE)
    procesado = models.BooleanField(blank=False, null=False, default=False)
    resultado_fogar_raw = models.TextField(blank=True)
    # TODO: Analizar conveniencia de usar jsonfields
    resultado_fogar_json = models.TextField(blank=True)
    identifier = models.PositiveIntegerField(default=0, unique=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    representacion_json = models.TextField(blank=True)

    def __str__( self ):
        return "Historial de Operacion detalle para id de Garantizar {0} - {1} ".format(self.operacionDetalle.id_garantizar, self.identifier)

    class Meta:
        verbose_name_plural = 'Historial de operaciones detalle'
        indexes = [models.Index(fields=['identifier', ]), ]
        app_label = 'api'


class OperacionEncoladaError(models.Model, UpdateMixin):
    id_garantizar = models.CharField(max_length=100, null=True, db_index=True)
    operacion = models.ForeignKey(Operacion, blank=False, null=False, on_delete=models.CASCADE)
    trace = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    # TODO: Analizar conveniencia de usar jsonfields
    representacion_json = models.TextField(blank=True)

    def __str__( self ):
        return "Id de Garantizar {0} - Id de Transacción {1}".format( self.id_garantizar, self.operacion.pk)

    class Meta:
        verbose_name_plural = 'Errores de operaciones detalle'
        app_label = 'api'


class GarantizarFogar(models.Model, UpdateMixin):
    id_garantizar = models.CharField(max_length=100, null=False, db_index=True)
    id_fogar = models.CharField(max_length=100, null=False, db_index=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True)

    def __str__( self ):
        return "Id de Garantizar {0} - Id de Fogar {1}".format( self.id_garantizar, self.id_fogar)

    class Meta:
        verbose_name_plural = 'Relacion Garantizar-Fogar'
        unique_together = ('id_garantizar', 'id_fogar',)
        app_label = 'api'
