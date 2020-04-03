# How to Dockerize a Celery App With Django And RabbitMQ (Dockerized)

Fuentes:

[Distributed Python - REPO](https://github.com/ZoomerAnalytics/python-celery-dockerize-celery-django)
[Documentación](https://www.distributedpython.com/2018/06/12/celery-django-docker/)

Docker and docker-compose are highly recommended to run the example.

* Levantar stack:

```docker-compose up -d```

* Rest APIs: 

http://localhost:8000 ```(middleware_api)```

http://localhost:8080 ```(fogar_mock)```

http://localhost:8090 ```(garantizar_mock)```

* DEMO - ALTA:

Simular alta de Garantizar (1)
```
POST http://localhost:8000/api/alta_garantias
BODY
{
    “url_respuesta” : “http://garantizarmock:8000/mock_resultado_garantias”,
    “operaciones”: [{
	  "id_garantizar": "1",
	  "datos_obligatorios": {
	    "cuit": "11222222223",
	    "tipoOperacion": "p",
	    "idRFGasociada": null,
	    "montoGarantizado": 1000,
	    "montoMaximoRefianzado": 1000
	  },
	  "datos_opcionales": {
	    "razonSocial": "ACME S.A.",
	    "fechaInstrumento": "20/07/2018",
	    "comisionDevengada": 15.5,
	    "numGarantiaSGR": "1111aaaa",
	    "fechaMonetizacion": "20/07/2018",
	    "fechaPrimerVencimiento": "01/09/2018",
	    "plazoTotal": 36,
	    "tipoTasaDeInteres": "FIJA",
	    "puntosPorcentuales": 25.5,
	    "sistemaDeAmortizacion": "FRANCES",
	    "frecuenciaDeAmortizacion": "MENSUAL",
	    "destinoDelPrestamo": "INVERSION PRODUCTIVA"
	  }
    },{
	  "id_garantizar": "2",
	  "datos_obligatorios": {
	    "cuit": "11222222223",
	    "tipoOperacion": "p",
	    "idRFGasociada": null,
	    "montoGarantizado": 1000,
	    "montoMaximoRefianzado": 1000
	  },
	  "datos_opcionales": {
	    "razonSocial": "ACME S.A.",
	    "fechaInstrumento": "20/07/2018",
	    "comisionDevengada": 15.5,
	    "numGarantiaSGR": "1111aaaa",
	    "fechaMonetizacion": "20/07/2018",
	    "fechaPrimerVencimiento": "01/09/2018",
	    "plazoTotal": 36,
	    "tipoTasaDeInteres": "FIJA",
	    "puntosPorcentuales": 25.5,
	    "sistemaDeAmortizacion": "FRANCES",
	    "frecuenciaDeAmortizacion": "MENSUAL",
	    "destinoDelPrestamo": "INVERSION PRODUCTIVA"
	  }
    },{
	  "id_garantizar": "3",
	  "datos_obligatorios": {
	    "cuit": "11222222223",
	    "tipoOperacion": "p",
	    "idRFGasociada": null,
	    "montoGarantizado": 1000,
	    "montoMaximoRefianzado": 1000
	  },
	  "datos_opcionales": {
	    "razonSocial": "ACME S.A.",
	    "fechaInstrumento": "20/07/2018",
	    "comisionDevengada": 15.5,
	    "numGarantiaSGR": "1111aaaa",
	    "fechaMonetizacion": "20/07/2018",
	    "fechaPrimerVencimiento": "01/09/2018",
	    "plazoTotal": 36,
	    "tipoTasaDeInteres": "FIJA",
	    "puntosPorcentuales": 25.5,
	    "sistemaDeAmortizacion": "FRANCES",
	    "frecuenciaDeAmortizacion": "MENSUAL",
	    "destinoDelPrestamo": "INVERSION PRODUCTIVA"
	  }
    },{
	  "id_garantizar": "4",
	  "datos_obligatorios": {
	    "cuit": "11222222223",
	    "tipoOperacion": "p",
	    "idRFGasociada": null,
	    "montoGarantizado": 1000,
	    "montoMaximoRefianzado": 1000
	  },
	  "datos_opcionales": {
	    "razonSocial": "ACME S.A.",
	    "fechaInstrumento": "20/07/2018",
	    "comisionDevengada": 15.5,
	    "numGarantiaSGR": "1111aaaa",
	    "fechaMonetizacion": "20/07/2018",
	    "fechaPrimerVencimiento": "01/09/2018",
	    "plazoTotal": 36,
	    "tipoTasaDeInteres": "FIJA",
	    "puntosPorcentuales": 25.5,
	    "sistemaDeAmortizacion": "FRANCES",
	    "frecuenciaDeAmortizacion": "MENSUAL",
	    "destinoDelPrestamo": "INVERSION PRODUCTIVA"
	  }
    },{
	  "id_garantizar": "5",
	  "datos_obligatorios": {
	    "cuit": "11222222223",
	    "tipoOperacion": "p",
	    "idRFGasociada": null,
	    "montoGarantizado": 1000,
	    "montoMaximoRefianzado": 1000
	  },
	  "datos_opcionales": {
	    "razonSocial": "ACME S.A.",
	    "fechaInstrumento": "20/07/2018",
	    "comisionDevengada": 15.5,
	    "numGarantiaSGR": "1111aaaa",
	    "fechaMonetizacion": "20/07/2018",
	    "fechaPrimerVencimiento": "01/09/2018",
	    "plazoTotal": 36,
	    "tipoTasaDeInteres": "FIJA",
	    "puntosPorcentuales": 25.5,
	    "sistemaDeAmortizacion": "FRANCES",
	    "frecuenciaDeAmortizacion": "MENSUAL",
	    "destinoDelPrestamo": "INVERSION PRODUCTIVA"
	  }
    },{
	  "id_garantizar": "6",
	  "datos_obligatorios": {
	    "cuit": "11222222223",
	    "tipoOperacion": "p",
	    "idRFGasociada": null,
	    "montoGarantizado": 1000,
	    "montoMaximoRefianzado": 1000
	  },
	  "datos_opcionales": {
	    "razonSocial": "ACME S.A.",
	    "fechaInstrumento": "20/07/2018",
	    "comisionDevengada": 15.5,
	    "numGarantiaSGR": "1111aaaa",
	    "fechaMonetizacion": "20/07/2018",
	    "fechaPrimerVencimiento": "01/09/2018",
	    "plazoTotal": 36,
	    "tipoTasaDeInteres": "FIJA",
	    "puntosPorcentuales": 25.5,
	    "sistemaDeAmortizacion": "FRANCES",
	    "frecuenciaDeAmortizacion": "MENSUAL",
	    "destinoDelPrestamo": "INVERSION PRODUCTIVA"
	  }
    },{
	  "id_garantizar": "7",
	  "datos_obligatorios": {
	    "cuit": "11222222223",
	    "tipoOperacion": "p",
	    "idRFGasociada": null,
	    "montoGarantizado": 1000,
	    "montoMaximoRefianzado": 1000
	  },
	  "datos_opcionales": {
	    "razonSocial": "ACME S.A.",
	    "fechaInstrumento": "20/07/2018",
	    "comisionDevengada": 15.5,
	    "numGarantiaSGR": "1111aaaa",
	    "fechaMonetizacion": "20/07/2018",
	    "fechaPrimerVencimiento": "01/09/2018",
	    "plazoTotal": 36,
	    "tipoTasaDeInteres": "FIJA",
	    "puntosPorcentuales": 25.5,
	    "sistemaDeAmortizacion": "FRANCES",
	    "frecuenciaDeAmortizacion": "MENSUAL",
	    "destinoDelPrestamo": "INVERSION PRODUCTIVA"
	  }
    },{
	  "id_garantizar": "8",
	  "datos_obligatorios": {
	    "cuit": "11222222223",
	    "tipoOperacion": "p",
	    "idRFGasociada": null,
	    "montoGarantizado": 1000,
	    "montoMaximoRefianzado": 1000
	  },
	  "datos_opcionales": {
	    "razonSocial": "ACME S.A.",
	    "fechaInstrumento": "20/07/2018",
	    "comisionDevengada": 15.5,
	    "numGarantiaSGR": "1111aaaa",
	    "fechaMonetizacion": "20/07/2018",
	    "fechaPrimerVencimiento": "01/09/2018",
	    "plazoTotal": 36,
	    "tipoTasaDeInteres": "FIJA",
	    "puntosPorcentuales": 25.5,
	    "sistemaDeAmortizacion": "FRANCES",
	    "frecuenciaDeAmortizacion": "MENSUAL",
	    "destinoDelPrestamo": "INVERSION PRODUCTIVA"
	  }
    },{
	  "id_garantizar": "9",
	  "datos_obligatorios": {
	    "cuit": "11222222223",
	    "tipoOperacion": "p",
	    "idRFGasociada": null,
	    "montoGarantizado": 1000,
	    "montoMaximoRefianzado": 1000
	  },
	  "datos_opcionales": {
	    "razonSocial": "ACME S.A.",
	    "fechaInstrumento": "20/07/2018",
	    "comisionDevengada": 15.5,
	    "numGarantiaSGR": "1111aaaa",
	    "fechaMonetizacion": "20/07/2018",
	    "fechaPrimerVencimiento": "01/09/2018",
	    "plazoTotal": 36,
	    "tipoTasaDeInteres": "FIJA",
	    "puntosPorcentuales": 25.5,
	    "sistemaDeAmortizacion": "FRANCES",
	    "frecuenciaDeAmortizacion": "MENSUAL",
	    "destinoDelPrestamo": "INVERSION PRODUCTIVA"
	  }
    },{
	  "id_garantizar": "10",
	  "datos_obligatorios": {
	    "cuit": "11222222223",
	    "tipoOperacion": "p",
	    "idRFGasociada": null,
	    "montoGarantizado": 1000,
	    "montoMaximoRefianzado": 1000
	  },
	  "datos_opcionales": {
	    "razonSocial": "ACME S.A.",
	    "fechaInstrumento": "20/07/2018",
	    "comisionDevengada": 15.5,
	    "numGarantiaSGR": "1111aaaa",
	    "fechaMonetizacion": "20/07/2018",
	    "fechaPrimerVencimiento": "01/09/2018",
	    "plazoTotal": 36,
	    "tipoTasaDeInteres": "FIJA",
	    "puntosPorcentuales": 25.5,
	    "sistemaDeAmortizacion": "FRANCES",
	    "frecuenciaDeAmortizacion": "MENSUAL",
	    "destinoDelPrestamo": "INVERSION PRODUCTIVA"
	  }
    }]	
}

RESPONSE 200 
	{
    "id_transaccion": 1,
    "total_operaciones_recibidas": 10,
    "ids_garantizar_encolados": [
      "1",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9",
      "10"
    ],
    "ids_garantizar_no_encolados": [],
    "ids_garantizar_sin_procesar": [],
    }
```

Mock de fogar (alta), responde con delay (2)
```
POST http://localhost:8080/mock_alta_garantia
HEADER
	Content-Type: application/json
BODY
	{
	  "id_garantizar": "1",
	  "datos_obligatorios": {
	    "cuit": "11222222223",
	    "tipoOperacion": "p",
	    "idRFGasociada": null,
	    "montoGarantizado": 1000,
	    "montoMaximoRefianzado": 1000
	  },
	  "datos_opcionales": {
	    "razonSocial": "ACME S.A.",
	    "fechaInstrumento": "20/07/2018",
	    "comisionDevengada": 15.5,
	    "numGarantiaSGR": "1111aaaa",
	    "fechaMonetizacion": "20/07/2018",
	    "fechaPrimerVencimiento": "01/09/2018",
	    "plazoTotal": 36,
	    "tipoTasaDeInteres": "FIJA",
	    "puntosPorcentuales": 25.5,
	    "sistemaDeAmortizacion": "FRANCES",
	    "frecuenciaDeAmortizacion": "MENSUAL",
	    "destinoDelPrestamo": "INVERSION PRODUCTIVA"
	  }
	}	

RESPONSE 201 
	{ 
	  "id_garantizar": "1", 
	  "id_fogar": "1", 
	  "message": "OK"
	}
```

NOTA: Cuando se encola una task en (1), su ejecución hace un request a (2).

----------

* DEMO - ACTUALIZACIÓN

Simular actualización de Garantizar (1)
Escenario: la garantia a actualizar no se encola dado que no hay registro previo del alta.
```
PUT http://localhost:8000/api/actualizacion_garantias
BODY 

{
    “url_respuesta” : “http://garantizarmock:8000/mock_resultado_garantias”,
    “operaciones”: [{
    "id_garantizar": "11",
    "id_fogar": "00000000001",
    "datos_actualizables": {
      "montoGarantizado": 1000.00,
      "destinoDelPrestamo": "CAPITAL DE TRABAJO"
      }
    }]
}

RESPONSE 200 
    {
    "id_transaccion": 2,
    "total_operaciones_recibidas": 1,
    "ids_garantizar_encolados": [],
    "ids_garantizar_no_encolados": [
      "11"
    ],
    "ids_garantizar_sin_procesar": [],
    }
```

Simular actualización de Garantizar (1)
Escenario: la garantia a actualizar se encola ok dado que hay registro previo del alta.
```
PUT http://localhost:8000/api/actualizacion_garantias
BODY 

{
    “url_respuesta” : “http://garantizarmock:8000/mock_resultado_garantias”,
    “operaciones”: [{
    "id_garantizar": "10",
    "id_fogar": "00000000001",
    "datos_actualizables": {
      "montoGarantizado": 1000.00,
      "destinoDelPrestamo": "CAPITAL DE TRABAJO"
      }
    }]
}

RESPONSE 200 
    {
    "id_transaccion": 3,
    "total_operaciones_recibidas": 1,
    "ids_garantizar_encolados": [
      "10"
    ],
    "ids_garantizar_no_encolados": [],
    "ids_garantizar_sin_procesar": [],
    }
```

Mock de fogar (actualización), responde con delay (2)
```
POST http://localhost:8080/mock_alta_garantia
HEADER
	Content-Type: application/json
BODY
	{
    "id_garantizar": "11",
    "id_fogar": "00000000001",
    "datos_actualizables": {
      "montoGarantizado": 1000.00,
      "destinoDelPrestamo": "CAPITAL DE TRABAJO"
      }
    }	

RESPONSE 201 
	{ 
	  "id_garantizar": "1", 
	  "id_fogar": "1", 
	  "message": "OK"
	}
```

NOTA: Cuando se encola una task en (1), su ejecución hace un request a (2).

* Monitor tasks in flower:

[http://localhost:5555](http://localhost:5555)

* Admin RabbitMQ 

[http://localhost:15672](http://localhost:15672)
user: user
pass: password

NOTA: si no se puede ingresar, probablemente sea porque no está activo el managment. Para activarlo hay que:

```
docker exec -it rabbit_broker bash

rabbitmq-plugins enable rabbitmq_management
```
AGREGARLE OPCION DE PODER AGREGAR RESULTADOS DE CELERY AL ADMIN
```
docker exec -it middleware_api bash
python manage.py migrate django_celery_results
```

## Crear superuser, inicializar estaticos y correr migrations (primera vez)

```
docker exec -it middleware_api bash
python manage.py migrate
python manage.py createsuperuser
admin
M0b34ts99
python manage.py collectstatic
```

## Ingresar a algunos de los containers

App celery
```
docker exec -it middleware_api bash

docker exec -it fogar_mock bash
```

## Crear usuario para "garantizar" y setear permisos para endpoints

* Con el stack levantado, ingresar a http://localhost:8000/admin/
* Ingresar a Users -> Add User
* Dar de alta usuario: 
	* Username: ```garantizar_fogar```
	* Password: ```g4r4nt1z4r```

Hasta aquí es suficiente para avanzar con la etapa de AUTHENTICATION. Sin embargo, para interactuar con ```/api/sample_api_garantizar``` y los endpoints específicos de garantizar será necesario configurar **Grupo** y **Permisos**:

* Crear nuevo permiso. Ingresar a Permissions -> Add permission
	* Name: ```Authorization_API```
	* Content type: ```user```
	* Codename: ```Authorization_API```

* Crear nuevo grupo. Ingresar a Groups -> Add group
	* Name: ```Garantizar```
	* Chosen permissions: ```auth | user | Authorization_API``` 	

* Agregar al **usuario garantizar_fogar** al grupo **Garantizar**
	* Ingresar a Users
	* Seleccionar al usuario garantizar_fogar
	* Chosen groups: Garantizar

## AUTHENTICATION (based on REST Framework)

[Token Based Authentication for Django Rest Framework](https://medium.com/quick-code/token-based-authentication-for-django-rest-framework-44586a9a56fb)

Login
```
POST http://localhost:8000/api/login
BODY
	{"username":"garantizar_fogar", "password":"g4r4nt1z4r"}

RESPONSE
	{"token": "904d9c1387cd42491d3e3e8194e846ffa8e7a6ca"}

```

Interactuando con recurso segurizado (que no requiere permisos)
```
GET http://localhost:8000/api/sample_secure_without_perms
HEADER
	Authorization: Token 904d9c1387cd42491d3e3e8194e846ffa8e7a6ca

RESPONSE 200 {"sample_data": 123}	
```

Interactuando con recurso segurizado (requiere que el usuario pertenezca al grupo Garantizar)
```
GET http://localhost:8000/api/sample_secure_garantizar	
HEADER
	Authorization: Token 904d9c1387cd42491d3e3e8194e846ffa8e7a6ca

RESPONSE 200 {"sample_data": 123}	
```

### Comandos docker útiles

* Para listar las imagenes de docker disponibles

```docker images```


* Para borrar una imagen docker

```docker rmi <IMAGE ID>```


* Para buildear una imagen, y levantar como daemon (requiere un dockerfile)

```docker-compose up -d --build```

```docker-compose up --force-recreate```


* Ver logs

```docker logs <ID container/image name>```
```docker-compose logs -f```

* Restart de un container

```docker-compose restart <image name>```

### Dependencias

* [DJ-Database-URL](https://github.com/kennethreitz/dj-database-url)
* celery==4.2.0
* Django==2.0.7
* djangorestframework==3.8.2
* requests==2.19.1

### Problemas de versiones

* Celery 4.2.0 con Python 3.7 
Error: AttributeError: module 're' has no attribute '_pattern_type'
Issue: fuentes varias
Solución: Downgrade a python 3.6

* Celery 4.1.1 
Error: Stuck in loop attempting to connect to RabbitMQ
Issue: https://github.com/celery/celery/issues/4895
Solución: Downgrade a celery 4.1.1



### CREAR MIGRACIONES POR APP (IDEM PARA CHECK POR APP)

```
python manage.py check nombreDeAPP
python manage.py makemigrations nombreDeAPP
python manage.py migrate nombreDeAPP
```

En este proyecto: 
> python manage.py check api