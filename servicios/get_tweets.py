# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------------------
# Archivo: get_tweets.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): Karina Chaires, Arturo Lagunas, Julio Gutiérrez.
# Version:  Mayo 2017
# Descripción:
#
# Este archivo define un rol de servicio. Su función principal es obtener los tweets con
# respecto a una película para posteriormente guardar estos tweets en una base de datos
# Este microservicio usa la API de twitter a través de la librería de Twython.
#
#
#
#                                        sv_sentimiento.py
#           +-----------------------+--------------------------+-----------------------------+
#           |  Nombre del elemento  |     Responsabilidad      |      Propiedades            |
#           +-----------------------+--------------------------+-----------------------------+
#	    |                       |  - Obtener los tweets    | - Utiliza la librería       |
#           |    Procesador de      |    que contengan comenta-|   Twython.                  |
#           |    tweets sobre       |    rios sobre una pelícu-| - Guarda los comentarios en |
#           |    una película	    |    la en particular      |   Redis sobre la película   |
#           |                       |    		       |   que se busca.     	     |
#	    |			    |			       | - Devuelve el títul de la   |
#	    |			    |			       |   película		     |
#           +-----------------------+--------------------------+-----------------------------+
#
#	Ejemplo de uso: Abrir navegador e ingresar a http://localhost:8084/api/v1/information?t=matrix
#
from twython import Twython
from slugify import slugify
import redis
import settings
import os
from flask import Flask, abort, render_template, request
import urllib, json
import sys
app = Flask (__name__)

# Llaves para identifocarse en la app
APP_KEY = 'MUebLOiElmDhgGoyFYZelhiMn'
APP_SECRET = 'eSJBb3LYEuN7XFV5U00IFBNtuWBgmsHPeUfPk8HkSxaIhTvMgR'
OAUTH_TOKEN = '2891574093-0FgmSMcryoJXoCOObTSneUALpRTSpqpo53WDuRj'
OAUTH_TOKEN_SECRET = 'QwC7VGrYjH9jo0eBKlR8cK8bHv6cUwLIzNzFKN4khfM5G'

#Se conecta con la API
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#Se conecra a Redis para poder guardar  los comentarips de tweeter
r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

#   Método para poder guardar los tweets
@app.route("/api/v1/tweets")
def get_tweets():
	
    # Se lee el parámetro 't' que contiene el título de la película o serie que se va a consultar
    title = request.args.get("t")
    #Se hace slug al nombre de la película
    title = slugify(title)
    #Se buscan los tweets de la película consultada
    resultados = twitter.search(q=title, count=50)
    #Se pasan a diccionario los datos obtenidos
    datos = resultados.keys()
    for i in range(len(resultados[datos[1]])):
	#Se saca el id del tweet
        id_title = resultados[datos[1]][i][u'id_str']
	#Se obtiene el texto del comentario
        text = resultados[datos[1]][i][u'text']
	#Se guardan los reultados en la Redis, el cual es una base de datos.
        r.set(title+":"+id_title,text)
    #Se regresa el nombre de la película para su posterior uso.
    return title
            

if __name__ == '__main__':
	# Se define el puerto del sistema operativo que utilizará el servicio
	port = int(os.environ.get('PORT', 8086))
	# Se habilita la opción de 'debug' para visualizar los errores
	app.debug = True
	# Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
	app.run(host='0.0.0.0', port=port)
