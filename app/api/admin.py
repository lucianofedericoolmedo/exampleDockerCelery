from django.contrib import admin
from django.contrib.auth.models import Permission
from django.urls import reverse
from django.utils.html import format_html
from . import models



def linkify(field_name,column_name):
    """
    Converts a foreign key value into clickable links.

    If field_name is 'parent', link text will be str(obj.parent)
    Link will be admin url for the admin url for obj.parent.id:change
    """
    def _linkify(obj):
        app_label = obj._meta.app_label
        linked_obj = getattr(obj, field_name)
        model_name = linked_obj._meta.model_name
        view_name = f"admin:{app_label}_{model_name}_change"
        link_url = reverse(view_name, args=[linked_obj.id])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = column_name # Sets column name
    return _linkify


class PermissionAdmin(admin.ModelAdmin):
    model = Permission
    list_display = ['id', 'name', 'content_type_id', 'codename', ]


class OperacionDetalleHistorialAdminTabular(admin.StackedInline):
    model = models.OperacionDetalleHistorial
    extra = 0
    readonly_fields = ['identifier', 'operacion', 'resultado_fogar_json', 'procesado', 'operacionDetalle',
                       'created_at', 'representacion_json', 'resultado_fogar_raw']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OperacionDetalleAdmin(admin.ModelAdmin):
    model = models.OperacionDetalle
    inlines = [OperacionDetalleHistorialAdminTabular, ]
    list_display = ('upper_case_name', linkify(field_name="operacion", column_name="Operacion de la que forma parte"),)
    list_filter = ['procesado']
    display_fields = ['id_garantizar', 'resultado_fogar_json', 'procesado',
                      'operacion', 'created_at', 'representacion_json', 'resultado_fogar_raw']
    readonly_fields = ['id_garantizar', 'resultado_fogar_json', 'procesado',
                       'operacion', 'created_at', 'representacion_json', 'status_code', 'resultado_fogar_raw']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def upper_case_name(self, obj):
        return "%s -- %s" % ("Detalle de operacion ",obj.id_garantizar)
    upper_case_name.short_description = 'Detalle de operacion'


class OperacionDetalleAdminTabular(admin.StackedInline):
    model = models.OperacionDetalle
    extra = 0
    readonly_fields = ['id_garantizar', 'operacion', 'resultado_fogar_json',
                       'procesado', 'created_at', 'representacion_json', 'status_code', 'resultado_fogar_raw']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OperacionDetalleHistorialAdmin(admin.ModelAdmin):
    model = models.OperacionDetalleHistorial
    list_filter = ['procesado']
    readonly_fields = ['identifier', 'operacion', 'resultado_fogar_json', 'procesado', 'operacionDetalle',
                       'created_at', 'representacion_json', 'resultado_fogar_raw']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OperacionAdmin(admin.ModelAdmin):
    model = models.Operacion
    inlines = [OperacionDetalleAdminTabular, OperacionDetalleHistorialAdminTabular]
    list_filter = ['resultado_enviado_garantizar','tipo_operacion']
    readonly_fields = ['tipo_operacion','total_operaciones','total_encoladas', 'total_no_encoladas',
                       'total_registro_previo', 'resultado_enviado_garantizar', 'resultado_generado_garantizar_json',
                       'respuesta_garantizar_json', 'total_encoladas_por_procesar', 'created_at', 'url_respuesta',
                       'representacion_json']

    def has_add_permission(self, request, obj=None):
        return False


class GarantizarFogarAdmin(admin.ModelAdmin):
    model = models.GarantizarFogar

    def has_add_permission(self, request, obj=None):
        return False

class OperacionEncoladaErrorAdmin(admin.ModelAdmin):
    model = models.OperacionEncoladaError

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Permission, PermissionAdmin)
admin.site.register(models.Operacion, OperacionAdmin)
admin.site.register(models.OperacionDetalle, OperacionDetalleAdmin)
admin.site.register(models.OperacionEncoladaError, OperacionEncoladaErrorAdmin)
admin.site.register(models.GarantizarFogar, GarantizarFogarAdmin)
admin.site.register(models.OperacionDetalleHistorial, OperacionDetalleHistorialAdmin)
