clave_garantizar = 'id_garantizar'
clave_datos_obligatorios = 'datos_obligatorios'
clave_datos_opcionales = 'datos_opcionales'
clave_datos_actualizacion = 'datos_actualizables'
clave_fogar = 'id_fogar'
clave_url = 'url_respuesta'
clave_garantias = 'operaciones'

max_retries_exceeded_status_code = 404
created_status_code = 201
conflict_status_code = 409

claves_garantia_metamodel_alta = [ 
    clave_garantizar,
    clave_datos_obligatorios,
    clave_datos_opcionales
]

claves_garantia_metamodel_actualizacion = [ 
    clave_garantizar,
    clave_fogar,
    clave_datos_actualizacion
]


campos_obligatorios = [
    "cuit", 
    "tipoOperacion",
    "idRFGasociada",
    "montoGarantizado",
    "montoMaximoRefianzado"
]

campos_opcionales = [
    "razonSocial",
    "fechaInstrumento",
    "comisionDevengada",
    "numGarantiaSGR",
    "fechaMonetizacion",
    "fechaPrimerVencimiento",
    "plazoTotal",
    "tipoTasaDeInteres",
    "puntosPorcentuales",
    "sistemaDeAmortizacion",
    "frecuenciaDeAmortizacion",
    "destinoDelPrestamo"
]

campos_actualizacion = campos_obligatorios + campos_opcionales

claves_diccionarios = [
    clave_datos_obligatorios,
    clave_datos_opcionales,
    clave_datos_actualizacion
]

claves_string = [
    clave_garantizar,
    clave_fogar
]


cuit_regex = "^[0-9]{2}[0-9]{8}[0-9]$"
currency_regex = '^(\d{1,})(\.\d{1,2})?$'
cuotas_regex = '^([1-9])?([0-9]{1,2})$'
porcentaje_regex = '^((100((\.|,)[0-9]{1,2})?)|([0-9]{1,2}((\.|,)[0-9]{0,2})?))$'
date_regex = '(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|((29|30)[\/](0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])(00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)'
tipo_tasa_de_interes_values = ['FIJA', 'BADLAR']
sistema_de_amortizacion_values = ['ALEMAN', 'FRANCES', 'AMERICANO']
frecuencia_de_amortizacion_values = ['MENSUAL', 'TRIMESTRAL', 'SEMESTRAL', 'ANUAL', 'AL VENCIMIENTO', 'CUATRIMESTRAL']
destino_del_prestamo_values = ['INVERSION PRODUCTIVA', 'CAPITAL DE TRABAJO', 'INVERSION PRODUCTIVA y CAPITAL DE TRABAJO', 'REFINANCIACION']
tipo_operacion_values = ['p', 'r']
idRFGasociada_regex = "^[0-9]{11}$]"