# -*- coding: utf-8 -*-

from . import models , garantia_checker_constants


def es_garantia_invalida(garantia_json):
	id_fogar = garantia_json[garantia_checker_constants.clave_fogar]
	id_garantizar = garantia_json[garantia_checker_constants.clave_garantizar]
	return not models.GarantizarFogar.objects.filter(id_garantizar=id_garantizar, id_fogar=id_fogar).exists()
