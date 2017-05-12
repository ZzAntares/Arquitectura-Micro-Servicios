# Arquitectura-Micro-Servicios

[![Build Status](https://travis-ci.org/ZzAntares/Arquitectura-Micro-Servicios.svg?branch=master)](https://travis-ci.org/ZzAntares/Arquitectura-Micro-Servicios)

Repositorio de la tarea 2


## Sistema de Procesamiento de Comentarios

Este proyecto muestra una interfaz web en la que puedes consultar información
sobre una película o serie y te muestra el sentimiento que genera en base al
análisis de los mensajes más relevantes encontrados en Twitter. Esta práctica se
realiza con el fin de conocer la implementación de la arquitectura de microservicios.


## Instalación

Antes de ejecutar el código asegúrate de instalar los prerrequisitos del sistema ejecutando:

``` shell
$ sudo pip install -r requirements.txt
```

Los paquetes que se instalarán son los siguientes:

Paquete     | Versión | Descripción
------------|---------|------------
Flask       | 0.10.1  | Micro framework de desarrollo
requests    | 2.12.4  | API interna utilizada en Flask para trabajar con las peticiones hacia el servidor
twython     | 3.4.0   | Cliente para comunicarse con el API de Twitter
slugify     | 0.0.1   | Librería para normalizar cadenas en formato de _slug_ `"Stranger Things" -> 'stranger-things'`
redis       | 2.10.5  | Driver de conexión a base de datos Python -> Redis
httpretty   | 0.8.14  | Librería para simular peticiones HTTP en pruebas
pytest      | 3.0.7   | Librería test-runner para ejecución de pruebas
mock        | 2.0.0   | Librería que simula atributos y comportamiento de objetos en pruebas
fakeredis   | 0.8.2   | Librería que simula una base de datos Redis para pruebas


Una vez instalados los prerrequisitos es momento de ejecutar el sistema siguiendo los siguientes pasos:

1. Ejecutar los servicios en terminales diferentes:

``` shell
$ python servicios/sv_information.py
$ python servicios/sv_tweets.py
$ python servicios/sv_sentimiento.py
```

2. Ejecutar el GUI:

``` shell
$ python gui.py
```

3. Abrir el navegador y acceder a la url del sistema:

```
http://localhost:8000/
```

## Nota sobre Redis

El sistema requiere acceso a un servidor de base de datos Redis, el proyecto
contiene una configuración en la cual se utiliza un servidor remoto por lo que
no es necesario que se instale Redis pero si es necesario contar con una
conexión a internet al ejecutar el proyecto ya que de no ser así el proyecto no
podrá hacer uso de la base de datos.

Si por el contrario se desea utilizar un servidor de Redis local o el servidor
remoto de Redis no está disponible, será necesario que se instale en la máquina
que ejecutará los microservicios de `sv_tweets.py` y `sv_sentimiento.py`.

Para instalar Redis en Ubuntu puede seguir estos pasos:

``` shell
$ sudo apt-get update && apt-get install redis-server  # Instalar redis
$ sudo service redis-server start                      # Inicia el servicio de redis
$ redis-cli ping                                       # En la pantalla se imprime 'PONG' si todo es correcto
```

Posteriormente es necesario cambiar la configuración del proyecto para que se
utilice la instancia local de Redis, para ello es necesario modificar el archivo
`services/settings.py` especificando los datos de conexión. Asumiendo que Redis
se ha instalado sin modificar ninguna configuración, se pueden utilizar los
siguientes datos:

```
# servicios/settings.py
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1
```

Una ves modificado y guardado este archivo es necesario reiniciar los
servicios de `sv_tweets.py` y `sv_sentimiento.py` para que los cambios
en la configuaración hagan efecto.


## Especificación de Microservicios (Blueprint)

La documentación esta disponible en el repositorio en la carpeta de `docs` o
también puede consultarse en línea a través de Apiary:

- [SV Information API](http://docs.svinformationapi.apiary.io/)
- [SV Tweets API](http://docs.svtweetsapi.apiary.io/)
- [SV Sentiment API](http://docs.svsentimentapi.apiary.io/)
