# -*- coding: utf-8 -*-

import re
from . import garantia_checker_helper , garantia_checker_constants, garantia_checker_model_helper


def obtener_diccionario_de_errores_de_validacion(elems):
    diccionario_de_errores = {}
    for clave_en_garantia in elems.keys():
        clave_a_evaluar = elems[clave_en_garantia]
        funcion_a_llamar, expresion_para_validacion = garantia_checker_helper.diccionario_de_reglas_de_validaciones[clave_en_garantia]
        funcion_a_llamar( clave_en_garantia, clave_a_evaluar, expresion_para_validacion , diccionario_de_errores)
    return diccionario_de_errores


def validate_clave_obligatorios_requerida(garantia):
    errores_de_validacion = {}
    
    if garantia_checker_constants.clave_datos_obligatorios not in garantia:
        return {'datos_obligatorios':{ 'falta_ingresar' : garantia_checker_constants.clave_datos_obligatorios}}

    if garantia[garantia_checker_constants.clave_datos_obligatorios] is None:
        errores_de_validacion = {
            garantia_checker_constants.clave_datos_obligatorios + ' incorrectos': "Ingrese un objeto para " +
                                                                                garantia_checker_constants.clave_datos_obligatorios}
        return {'datos_obligatorios': errores_de_validacion}

    if type(garantia[garantia_checker_constants.clave_datos_obligatorios]) is not dict:
        errores_de_validacion = {
            garantia_checker_constants.clave_datos_obligatorios + ' incorrectos': "Ingrese un objeto para " +
                                                                                garantia_checker_constants.clave_datos_obligatorios}
        return {'datos_obligatorios': errores_de_validacion}

    if len(garantia[garantia_checker_constants.clave_datos_obligatorios].keys()) == 0:
        errores_de_validacion = {
            garantia_checker_constants.clave_datos_obligatorios + ' incorrectos': "Ingrese valores para el objeto en " +
                                                                                garantia_checker_constants.clave_datos_obligatorios}
        return {'datos_opcionales': errores_de_validacion}

    elems = garantia[garantia_checker_constants.clave_datos_obligatorios].keys()
    incorrectas = garantia_checker_helper.has_unmatch_keys(elems, garantia_checker_constants.campos_obligatorios)
    sin_completar = garantia_checker_helper.has_unmatch_keys(garantia_checker_constants.campos_obligatorios, elems)

    if len(incorrectas) > 0:
        # Agregar s en incorrectos si es mayor a 1
        incorrectas = ','.join(incorrectas)
        value = { 'incorrectos' : incorrectas}
        errores_de_validacion.update(value)

    if len(sin_completar) > 0:
        sin_completar = ','.join(sin_completar)
        value = { 'sin_completar' : sin_completar}
        errores_de_validacion.update(value)

    if len(incorrectas) == 0 and len(sin_completar) == 0:
        regex_reasons = obtener_diccionario_de_errores_de_validacion(
            garantia[garantia_checker_constants.clave_datos_obligatorios])
        errores_de_validacion.update(regex_reasons)
    
    if len(errores_de_validacion.values()) > 0:
        return {'datos_obligatorios' : errores_de_validacion}

    return errores_de_validacion


def validate_clave_opcionales(garantia):
    errores_de_validacion = {}
    if garantia_checker_constants.clave_datos_opcionales in garantia:

        if garantia[garantia_checker_constants.clave_datos_opcionales] is None:
            errores_de_validacion = {garantia_checker_constants.clave_datos_opcionales + ' incorrectos': "Ingrese un objeto para " +
                                                                                                            garantia_checker_constants.clave_datos_opcionales}
            return {'datos_opcionales': errores_de_validacion}

        if type(garantia[garantia_checker_constants.clave_datos_opcionales]) is not dict:
            errores_de_validacion = {
                garantia_checker_constants.clave_datos_opcionales + ' incorrectos': "Ingrese un objeto para " +
                                                                                       garantia_checker_constants.clave_datos_opcionales}
            return {'datos_opcionales': errores_de_validacion}

        if len(garantia[garantia_checker_constants.clave_datos_opcionales].keys()) == 0:
            errores_de_validacion = {
                garantia_checker_constants.clave_datos_opcionales + ' incorrectos': "Ingrese valores para el objeto en " +
                                                                                       garantia_checker_constants.clave_datos_opcionales}
            return {'datos_opcionales': errores_de_validacion}


        else:
            elems = garantia[garantia_checker_constants.clave_datos_opcionales].keys()
            incorrectas = garantia_checker_helper.has_unmatch_keys(elems,
                                                                   garantia_checker_constants.campos_opcionales)
            if len(incorrectas) > 0:
                # Agregar s en incorrectos si es mayor a 1
                incorrectas = ', '.join(incorrectas)
                errores_de_validacion = {garantia_checker_constants.clave_datos_opcionales + ' incorrectos' : incorrectas}

            else:
                regex_reasons = obtener_diccionario_de_errores_de_validacion(
                    garantia[garantia_checker_constants.clave_datos_opcionales])
                errores_de_validacion = regex_reasons
        
    if len(errores_de_validacion.values()) > 0:
        return {'datos_opcionales' : errores_de_validacion}
    return errores_de_validacion


def validate_clave_actualizables(garantia):
    errores_de_validacion = {}

    if garantia_checker_constants.clave_datos_actualizacion not in garantia:
        return {'datos_actualizables':{ 'falta_ingresar' : garantia_checker_constants.clave_datos_actualizacion}}

    if garantia_checker_constants.clave_datos_actualizacion in garantia:
        if garantia[garantia_checker_constants.clave_datos_actualizacion] is None:
            errores_de_validacion = {garantia_checker_constants.clave_datos_actualizacion + ' incorrectos': "Ingrese un objeto para " +
                                                                                                            garantia_checker_constants.clave_datos_actualizacion}
            return {'datos_actualizables': errores_de_validacion}

        if type(garantia[garantia_checker_constants.clave_datos_actualizacion]) is not dict:
            errores_de_validacion = {
                garantia_checker_constants.clave_datos_actualizacion + ' incorrectos': "Ingrese un objeto para " +
                                                                                       garantia_checker_constants.clave_datos_actualizacion}
            return {'datos_actualizables': errores_de_validacion}


        if len(garantia[garantia_checker_constants.clave_datos_actualizacion].keys()) == 0:
            errores_de_validacion = {
                garantia_checker_constants.clave_datos_actualizacion + ' incorrectos': "Ingrese valores para el objeto en " +
                                                                                       garantia_checker_constants.clave_datos_actualizacion}
            return {'datos_actualizables': errores_de_validacion}

        else:
            elems = garantia[garantia_checker_constants.clave_datos_actualizacion].keys()
            incorrectas = garantia_checker_helper.has_unmatch_keys(elems,
                                                                   garantia_checker_constants.campos_actualizacion)
            if len(incorrectas) > 0:
                # Agregar s en incorrectos si es mayor a 1
                incorrectas = ', '.join(incorrectas)
                errores_de_validacion = {garantia_checker_constants.clave_datos_actualizacion + ' incorrectos' : incorrectas}

            else:
                regex_reasons = obtener_diccionario_de_errores_de_validacion(
                    garantia[garantia_checker_constants.clave_datos_actualizacion])
                errores_de_validacion = regex_reasons
        
    if len(errores_de_validacion.values()) > 0:
        return {'datos_actualizables' : errores_de_validacion}
    return errores_de_validacion


def obtener_invalidas_template(garantia_dict, claves_metamodel, bloques_de_funciones, esActualizar):

    if type(garantia_dict) is not dict: 
        return [{'Error': 'La estructura informada no cumple la especificación'}]

    if garantia_checker_constants.clave_url not in garantia_dict:
        return [{'Error ' + garantia_checker_constants.clave_url : 'Debe enviar ' + garantia_checker_constants.clave_url}]

    if type(garantia_dict[garantia_checker_constants.clave_url]) is not str: 
        return [{'Error ' + garantia_checker_constants.clave_url : 'Valor inválido'}]

    is_empty_string = not bool(garantia_dict[garantia_checker_constants.clave_url].strip())
    if is_empty_string:
        return [{'Error ' + garantia_checker_constants.clave_url: 'Ingrese un valor valido'}]

    if garantia_checker_constants.clave_garantias not in garantia_dict:
        return [{'Error ' + garantia_checker_constants.clave_garantias: 'Debe enviar ' + garantia_checker_constants.clave_garantias}]

    if type(garantia_dict[garantia_checker_constants.clave_garantias]) is not list: 
        return [{'Error ' + garantia_checker_constants.clave_garantias: 'Se requiere una lista con al menos 1 (una) operación para procesar'}]

    errores_de_validacion_de_garantias = []

    garantias = garantia_dict[garantia_checker_constants.clave_garantias]

    for garantia in garantias:
        errores_de_validacion_de_garantia = {}

        esta_fogar = garantia_checker_constants.clave_fogar in garantia 
        esta_garantizar = garantia_checker_constants.clave_garantizar in garantia
        no_esta_fogar = garantia_checker_constants.clave_fogar not in garantia 
        no_esta_garantizar = garantia_checker_constants.clave_garantizar not in garantia


        #id garantizar
        if no_esta_garantizar:
            errores_de_validacion_de_garantia['Error'] = 'Falta ingresar ' + garantia_checker_constants.clave_garantizar
            errores_de_validacion_de_garantias.append(errores_de_validacion_de_garantia)
            continue
        
        if esta_garantizar:
            if garantia[garantia_checker_constants.clave_garantizar] is None:
                errores_de_validacion_de_garantia['Error'] = 'Falta ingresar ' + garantia_checker_constants.clave_garantizar
                errores_de_validacion_de_garantias.append(errores_de_validacion_de_garantia)
                continue

            if type(garantia[garantia_checker_constants.clave_garantizar]) is not str:
                errores_de_validacion_de_garantia['Error'] = 'Tipo de dato incorrecto ' + garantia_checker_constants.clave_garantizar
                errores_de_validacion_de_garantias.append(errores_de_validacion_de_garantia)
                continue

        initial_key = "=".join([garantia_checker_constants.clave_garantizar ,
                                garantia[garantia_checker_constants.clave_garantizar]])

        # id fogar
        if no_esta_fogar and esActualizar:
            errores_de_validacion_de_garantia[
                'Error de clave Fogar'] = 'Falta ingresar ' + garantia_checker_constants.clave_fogar
            errores_de_validacion_de_garantias.append(errores_de_validacion_de_garantia)
            continue

        # id fogar y es null
        if esta_fogar and esActualizar:
            if garantia[garantia_checker_constants.clave_fogar] is None:
                errores_de_validacion_de_garantia[initial_key] = {}
                errores_de_validacion_de_garantia[initial_key].update({garantia_checker_constants.clave_fogar : 'No puede ser nulo'})
                errores_de_validacion_de_garantias.append(errores_de_validacion_de_garantia)
                continue

            if type(garantia[garantia_checker_constants.clave_fogar]) is not str:
                errores_de_validacion_de_garantia[initial_key] = {}
                errores_de_validacion_de_garantia[initial_key].update(
                    {garantia_checker_constants.clave_fogar: 'Tiene que ser un string'})
                errores_de_validacion_de_garantias.append(errores_de_validacion_de_garantia)
                continue


        #Validacion relacion entre Fogar Y Garantizar IDs        
        estan_garantizar_y_fogar = esta_fogar and esta_garantizar and esActualizar
        if estan_garantizar_y_fogar and garantia_checker_model_helper.es_garantia_invalida(garantia):
            errores_de_validacion_de_garantia[initial_key] = {}
            errores_de_validacion_de_garantia[initial_key].update({'Inconsistencia' : 'La clave ' +
                garantia_checker_constants.clave_fogar + ' es incompatible con ' + 
                garantia_checker_constants.clave_garantizar})
            errores_de_validacion_de_garantias.append(errores_de_validacion_de_garantia)
            continue
        

        claves_instancia_garantia = garantia.keys()
        claves_principales_sin_coincidir_entre_garantia_y_metamodelo = garantia_checker_helper.has_unmatch_keys(claves_metamodel, 
            claves_instancia_garantia)

        if len(claves_principales_sin_coincidir_entre_garantia_y_metamodelo) > 0:
            claves_principales_sin_coincidir_entre_garantia_y_metamodelo = ", ".join(claves_principales_sin_coincidir_entre_garantia_y_metamodelo)
            errores_de_validacion_de_garantia[initial_key] = {}
            errores_de_validacion_de_garantia[initial_key].update({'claves_faltantes_o_mal_ingresadas' : 
                claves_principales_sin_coincidir_entre_garantia_y_metamodelo})
            errores_de_validacion_de_garantias.append(errores_de_validacion_de_garantia)
            continue

        else:
            errores_de_validacion_de_garantia[initial_key] = {}
            for funcion_a_aplicar in bloques_de_funciones:
                errores_de_validacion_de_garantia[initial_key].update(funcion_a_aplicar(garantia))
        
        errores_de_validacion_de_garantia[initial_key] = {}
        
        for funcion_a_aplicar in bloques_de_funciones:
            errores_de_validacion_de_garantia[initial_key].update(funcion_a_aplicar(garantia))
        
        if len(errores_de_validacion_de_garantia[initial_key].values()) > 0:
            errores_de_validacion_de_garantias.append(errores_de_validacion_de_garantia)

    return errores_de_validacion_de_garantias


def errores_en_campos_en_alta(garantias):
    return obtener_invalidas_template(garantias,garantia_checker_constants.claves_garantia_metamodel_alta,
        [validate_clave_obligatorios_requerida,validate_clave_opcionales], False)


def errores_en_campos_en_actualizacion(garantias):
    return obtener_invalidas_template(garantias,garantia_checker_constants.claves_garantia_metamodel_actualizacion,
        [validate_clave_actualizables], True)