# Arquitectura-Micro-Servicios
Repositorio de la tarea 2


## Sistema de Procesamiento de Comentarios

Este proyecto muestra una interfaz web en la que puedes consultar información
sobre una película o serie y te muestra el sentimiento que genera en base al
análisis de los mensajes más relevantes encontrados en Twitter.


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
slugify     | 0.0.1   | Librería para normalizar cadenas en formato de /slug/ `"Stranger Things -> 'stranger-things'"`
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

TODO: Agregar nota sobre redis
*Nota:* A pesar de que el sistema requiere conexión con la base de datos Redis
no es necesario instalar


## Especificación de Microservicios (Blueprint)

La documentación esta disponible en el repositorio en la carpeta de `docs` o
también puede consultarse en línea a través de Apiary:

- [SV Information API](http://docs.svinformationapi.apiary.io/)
- [SV Tweets API](http://docs.svtweetsapi.apiary.io/)
- [SV Sentiment API](http://docs.svsentimentapi.apiary.io/)
