# -*- coding: utf-8 -*-

import re

from . import garantia_checker_constants

clave_inicial_requerida = garantia_checker_constants.clave_garantizar
clave_obligatorios_requerida = garantia_checker_constants.clave_datos_obligatorios
clave_opcionales = garantia_checker_constants.clave_datos_opcionales
claves_garantia_metamodel_alta = garantia_checker_constants.claves_garantia_metamodel_alta
claves_obligatorios = garantia_checker_constants.campos_obligatorios
claves_opcionales = garantia_checker_constants.campos_opcionales
clave_actualizacion = garantia_checker_constants.clave_datos_actualizacion
claves_garantia_metamodel_actualizacion = garantia_checker_constants.claves_garantia_metamodel_actualizacion
claves_actualizacion = garantia_checker_constants.campos_actualizacion

cuit_regex = garantia_checker_constants.cuit_regex
currency_regex = garantia_checker_constants.currency_regex
cuotas_regex = garantia_checker_constants.cuotas_regex
porcentaje_regex = garantia_checker_constants.porcentaje_regex
idRFGasociada_regex = garantia_checker_constants.idRFGasociada_regex
date_regex = garantia_checker_constants.date_regex
tipo_tasa_de_interes_values = garantia_checker_constants.tipo_tasa_de_interes_values
sistema_de_amortizacion_values = garantia_checker_constants.sistema_de_amortizacion_values
frecuencia_de_amortizacion_values = garantia_checker_constants.frecuencia_de_amortizacion_values
destino_del_prestamo_values = garantia_checker_constants.destino_del_prestamo_values
tipo_operacion_values = garantia_checker_constants.tipo_operacion_values


def has_unmatch_keys(one_set_of_keys,other_set_of_keys):
    keys_reason = []
    for key in one_set_of_keys:
        if key not in other_set_of_keys:
            keys_reason.append(key)
    return keys_reason
    

def validate_clave_inicial_requerida(garantia):
    invalid_reasons = []
    if clave_inicial_requerida not in garantia:
        invalid_reasons.append(clave_inicial_requerida)

    if clave_inicial_requerida in garantia:
        if type(garantia[clave_inicial_requerida]) != str:
            invalid_reasons.append(clave_inicial_requerida + " debe ser un String")
    return invalid_reasons


def check_field_string_with_regex( field_to_match, supossed_string_to_check, regex_string, error_elems):    
    if type(supossed_string_to_check) is str:   
        pattern = re.compile(regex_string)
        if not pattern.match(supossed_string_to_check):
            value_elem = supossed_string_to_check + " no es valido como " + field_to_match
            error = { field_to_match : value_elem }  
            error_elems.update(error)  
    else:
        error = { field_to_match : "No es un string" }
        error_elems.update(error)  

def check_field_number_with_regex( field_to_match, supossed_number_to_check, regex_string, error_elems):   

    if type(supossed_number_to_check) is int or type(supossed_number_to_check) is float:   
        supossed_string_to_check = str(supossed_number_to_check)
        pattern = re.compile(regex_string)

        if not pattern.match(supossed_string_to_check):
            value_elem = supossed_string_to_check + " no es valido como " + field_to_match
            error = { field_to_match : value_elem } 
            error_elems.update(error)  
    else:
        error = { field_to_match : "No cumple con " +  regex_string}
        error_elems.update(error)


def check_field_number_with_porcentaje_regex( field_to_match, supossed_number_to_check, regex_string, error_elems):

    if type(supossed_number_to_check) is int or type(supossed_number_to_check) is float:
        supossed_string_to_check = str(supossed_number_to_check)
        pattern = re.compile(regex_string)

        if not pattern.match(supossed_string_to_check):
            value_elem = supossed_string_to_check + " no es valido como " + field_to_match
            error = { field_to_match : value_elem }
            error_elems.update(error)
    else:
        error = { field_to_match : "No es un porcentaje valido"}
        error_elems.update(error)


def check_field_number_until( field_to_match, supossed_number_to_check, min_max_tuple, error_elems):
    min_comp , max_comp = min_max_tuple
    if type(supossed_number_to_check) is int or type(supossed_number_to_check) is float:
        supossed_string_to_check = str(supossed_number_to_check)
        if supossed_number_to_check < min_comp:
            value_elem = supossed_string_to_check + " es menor a " + str(min_comp) + " (mínimo admitido)"
            error = { field_to_match : value_elem }
            error_elems.update(error)
        
        if supossed_number_to_check > max_comp:
            value_elem = supossed_string_to_check + " es mayor a " + str(max_comp) + " (máximo admitido)"
            error = { field_to_match : value_elem }
            error_elems.update(error)
    else:
        error = { field_to_match : "No es un numero valido"}
        error_elems.update(error)


def check_field_number_optional_with_regex( field_to_match, supossed_number_to_check, regex_string, error_elems):   
    if  supossed_number_to_check is not None:
        check_field_number_with_regex( field_to_match, supossed_number_to_check, regex_string, error_elems)


def check_field_string_optional_with_regex( field_to_match, supossed_string_to_check, regex_string, error_elems):   
    if  supossed_string_to_check is not None:
        check_field_string_with_regex( field_to_match, supossed_string_to_check, regex_string, error_elems)


def check_field_number_with_specific_values( field_to_match, supossed_number_to_check, specific_values,error_elems):    
    if type(supossed_number_to_check) is int or type(supossed_number_to_check) is float:
        if supossed_number_to_check not in specific_values:
            error = { field_to_match : "No matchea " + supossed_number_to_check + " con "+ specific_values} 
            error_elems.update(error)  
    else:
        error = { field_to_match : "No matchea con "+ specific_values}
        error_elems.update(error)  


def check_field_string_with_specific_values(field_to_match,  supossed_string_to_check, specific_values, error_elems):   
    specific_values = ", ".join(specific_values)
    if type(supossed_string_to_check) is str:
        is_empty_string = not bool(supossed_string_to_check.strip())
        if is_empty_string:
            error = {field_to_match: 'Ingrese un valor dentro de ' + specific_values}
            error_elems.update(error)
        else:
            if supossed_string_to_check not in specific_values:
                value_elem = supossed_string_to_check + " no matchea con " + specific_values
                error = { field_to_match : value_elem }
                error_elems.update(error)
    else:
        error = {field_to_match : 'Ingrese un valor dentro de ' + specific_values}
        error_elems.update(error)  


def check_field_string( field_to_match, field_to_evaluate, comparison_operand, error_elems):
    value_elem = {field_to_match : "Debe ingresar un valor valido"}
    if field_to_evaluate is not None:
        if type(field_to_evaluate) is str:
            if field_to_evaluate.strip() == comparison_operand:
                return error_elems.update(value_elem)
    else:
        return error_elems.update(value_elem)


def check_field_date_with_regex(field_to_match, supossed_string_to_check, regex_string, error_elems):
    if supossed_string_to_check is None :
        value_elem = "Ingrese una fecha valida"
        error = {field_to_match: value_elem}
        error_elems.update(error)
        return

    is_empty_string = not bool(supossed_string_to_check.strip())
    if is_empty_string:
        value_elem = "Ingrese una fecha valida"
        error = {field_to_match: value_elem}
        error_elems.update(error)
        return

    else:
        value_elem = str(supossed_string_to_check) + " no es una fecha valida "
        error = { field_to_match :  value_elem }

        if type(supossed_string_to_check) is str:
            pattern = re.compile(regex_string)
            if not pattern.match(supossed_string_to_check):
                error_elems.update(error)
        else:
            error_elems.update(error)


def check_field_currency_number_with_regex( field_to_match, supossed_number_to_check, regex_string, error_elems):   
    if type(supossed_number_to_check) is int or type(supossed_number_to_check) is float:   
        supossed_string_to_check = str(supossed_number_to_check)
        pattern = re.compile(regex_string)

        if not pattern.match(supossed_string_to_check):
            error = { field_to_match : supossed_string_to_check + " no es un monto valido"} 
            error_elems.update(error)  
    else:
        error = { field_to_match : "Ingrese un monto valido"} 
        error_elems.update(error)


diccionario_de_reglas_de_validaciones= {
    "cuit" : (check_field_string_with_regex ,cuit_regex),
    "tipoOperacion": (check_field_string_with_specific_values ,tipo_operacion_values), 
    "idRFGasociada": (check_field_string_optional_with_regex, idRFGasociada_regex),
    "montoGarantizado": (check_field_currency_number_with_regex, currency_regex ),
    "montoMaximoRefianzado": (check_field_currency_number_with_regex, currency_regex ),
    "razonSocial" : (check_field_string ,""),
    "numGarantiaSGR" : (check_field_string, ""),
    "fechaInstrumento" : (check_field_date_with_regex ,date_regex),
    "comisionDevengada" : (check_field_number_with_porcentaje_regex ,porcentaje_regex),
    "fechaMonetizacion" : (check_field_date_with_regex ,date_regex),
    "fechaPrimerVencimiento" : (check_field_date_with_regex ,date_regex),
    "plazoTotal" : (check_field_number_until, (1,9999) ),
    "tipoTasaDeInteres": (check_field_string_with_specific_values ,tipo_tasa_de_interes_values), 
    "puntosPorcentuales": (check_field_number_with_regex, porcentaje_regex ),
    "sistemaDeAmortizacion": (check_field_string_with_specific_values , sistema_de_amortizacion_values),
    "frecuenciaDeAmortizacion": (check_field_string_with_specific_values ,frecuencia_de_amortizacion_values),
    "destinoDelPrestamo": (check_field_string_with_specific_values , destino_del_prestamo_values)
}
