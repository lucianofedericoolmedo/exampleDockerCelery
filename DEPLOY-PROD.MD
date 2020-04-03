## Build de imagenes

* Dockerfile_api -> middleware_garantizar/api

```
docker build -f Dockerfile_api -t middleware_garantizar/api:latest .
docker run -it -p 8000:8000 middleware_garantizar/api
```

TAG:
```
docker tag middleware_garantizar/api:VERSION hub.mobeats.com.ar/middleware_garantizar/api:VERSION
```

PUSH:
```
docker push hub.mobeats.com.ar/middleware_garantizar/api:VERSION
```

* Dockerfile_worker_entrada -> middleware_garantizar/worker_entrada

```
docker build -f Dockerfile_worker_entrada -t middleware_garantizar/worker_entrada:latest .
docker run -it middleware_garantizar/worker_entrada
```

TAG:
```
docker tag middleware_garantizar/worker_entrada:VERSION hub.mobeats.com.ar/middleware_garantizar/worker_entrada:VERSION
```

PUSH:
```
docker push hub.mobeats.com.ar/middleware_garantizar/worker_entrada:VERSION
```

* Dockerfile_worker_salida -> middleware_garantizar/worker_salida

```
docker build -f Dockerfile_worker_salida -t middleware_garantizar/worker_salida:latest .
docker run -it middleware_garantizar/worker_salida
```

TAG:
```
docker tag middleware_garantizar/worker_salida:VERSION hub.mobeats.com.ar/middleware_garantizar/worker_salida:VERSION
```

PUSH:
```
 docker push hub.mobeats.com.ar/middleware_garantizar/worker_salida:VERSION
```

* Dockerfile_mock_fogar -> middleware_garantizar/mock_fogar

```
docker build -f Dockerfile_mock_fogar -t middleware_garantizar/mock_fogar:latest .
docker run -it -p 8080:8000 middleware_garantizar/mock_fogar
```

TAG:
```
docker tag middleware_garantizar/mock_fogar:VERSION hub.mobeats.com.ar/middleware_garantizar/mock_fogar:VERSION
```

PUSH:
```
docker push hub.mobeats.com.ar/middleware_garantizar/mock_fogar:VERSION
```

* Dockerfile_mock_garantizar -> middleware_garantizar/mock_garantizar

```
docker build -f Dockerfile_mock_garantizar -t middleware_garantizar/mock_garantizar:latest .
docker run -it -p 8090:8000 middleware_garantizar/mock_garantizar
```

TAG:
```
docker tag middleware_garantizar/mock_garantizar:VERSION hub.mobeats.com.ar/middleware_garantizar/mock_garantizar:VERSION
```

PUSH:
```
docker push hub.mobeats.com.ar/middleware_garantizar/mock_garantizar:VERSION
```

# Accesos ambiente QA / Prod

::Admin -> http://garantizarws.mobeats.com.ar/admin/
User: admin
Pass: M0b34ts99

::Garantizar
User: garantizar_fogar
Pass: g4r4nt1z4r

::Flower
http://192.168.6.250:5555/

::DB
http://192.168.6.250:3306
User/Pass: ver docker-compose