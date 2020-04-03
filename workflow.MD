

-----------------------------------------------------------------------------------
LLEGA EL REQUEST
-----------------------------------------------------------------------------------

Crea Operacion (id_T (ver mejor forma (autoincremental ??), cant, por_procesar =  len(request.data)) 

For elem in request.data:
  Creo OperacionDetalle (id_T = Operacion, id_garantizar = elem.id_garantizar, procesado = false)
  C = toda la info a procesar 
  #Falta todo lo de encolar

Retorno la info de Operacion (o Operacion serializado), status 201
-----------------------------------------------------------------------------------


-----------------------------------------------------------------------------------
AGREGAR BUFFER DE SALIDA
-----------------------------------------------------------------------------------
Persisto respuesta de fogar.
Cada response de fogar hace un chequeo en los OperacionDetalle ( busca por id_garantizar los pone procesados) y dado el id_t (FK a Operacion) del OperacionDetalle, tomarlo para buscar el Operacion correspondiente y descontarle a dicho Operacion 1 en el campo por_procesar) .
Dado un op incluido en Operacion , si op.por_procesar == 0 (TRANSACCIONAL) => pre-enviar a cola de salida , op > 0, la task termina.
-----------------------------------------------------------------------------------



-----------------------------------------------------------------------------------
PRE-ENVIAR LA COLA DE SALIDA
-----------------------------------------------------------------------------------
PRECONDICION = Ya sabes que el buffer de salida ya fueron procesados

Traer de la BD, todas las operaciones procesadas con id_T = X,
Generar el obj de respuesta
Y recien ahi, encolar respuesta a la cola de salida
-----------------------------------------------------------------------------------


--------------------------------------MODELOS -----------------------------------------

------- Operacion  -------------

id_T , total, por_procesar

-----------------------------------------------------

--------- OperacionDetalle ---------

id_garantizar, procesado:Boolean, id_T (FK), 




