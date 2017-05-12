# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------------------
# Archivo: sv_sentimiento.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): Karina Chaires, Arturo Lagunas, Julio Gutiérrez.
# Version:  Mayo 2017
# Descripción:
#
#   Este archivo define el rol de un servicio. Su función general es porporcionar en un objeto JSON
#   información acerca del sentimiento de los comentarios en twitter de una pelicula o una serie en particular haciendo uso del API proporcionada
#   por mashape ('https://text-sentiment.p.mashape.com/analyze').
#
#
#
#                                        sv_sentimiento.py
#           +-----------------------+--------------------------+---------------------------------------------+
#           |  Nombre del elemento  |     Responsabilidad      |      Propiedades                            |
#           +-----------------------+--------------------------+---------------------------------------------+
#           |                       |  - Ofrecer un JSON que   | - Utiliza el API de                         |
#           |    Procesador de      |    contenga el sentimien-|   mashape.                                  |
#           |    sentimientos       |    to de los comentarios | - Devuelve un JSON con el total de          |
#           |    de mashape         |    en tw de películas o  |   sentimiento positivos, negativos, neutros |
#           |                       |    series en particular. |   de la serie o pelicula en cuestión.       |
#           +-----------------------+--------------------------+---------------------------------------------+
#
#	Ejemplo de uso: Abrir navegador e ingresar a http://localhost:8085/api/v1/sentimiento?t=matrix
#
import os
from flask import Flask, abort, render_template, request
from slugify import slugify
import urllib, json, requests, settings, redis

app = Flask (__name__)
r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

@app.route("/api/v1/sentimiento")
def get_analyze():
	# Método que obtiene la información del sentimiento acerca de un título en particular
	# Se lee el parámetro 't' que contiene el título de la película o serie que se va a consultar
	title = request.args.get("t")
	#Se hace slug al nombre de la película
	title = slugify(title)
	# Se verifica si el parámetro no esta vacío
	if title is not None:
		# Se obtiene la respuesta de analisis
		resultado = get_tweets(title)
		# Se regresa el JSON de la respuesta
		return resultado
 	else:
 		# Se devuelve un error 400 para indicar que el servicio no puede funcionar sin parámetro
 		abort(400)

def get_sentiment_tw(text):
	# Método que obtiene la información del sentimiento acerca de un título en particular
	# Se verifica si el parámetro no esta vacío
	if not text:
 		# Se devuelve un error 400 para indicar que el servicio no puede funcionar sin parámetro
 		abort(400)

	# Se conecta con el servicio de mashape a través de su API
	endpoint = 'http://text-processing.com/api/sentiment/'
	headers = {
		# 'X-Mashape-Key': settings.MASHAPE_KEY,
		"Content-Type": "application/x-www-form-urlencoded",
		"Accept": "application/json"
	}

	# Se envían los paramétros al API
	params = {
		# 'language': 'english',
		'text': text,
	}

	# Se obtiene la respuesta de mashape
	resultado = requests.post(endpoint, headers=headers, data=params)
	# {"lang": "ENGLISH", "totalLines": 1, "text": "I am not really happy", "mid_percent": "0%", "mid": 0, "pos": 0, "pos_percent": "0%", "neg": 1, "neg_percent": "100%"}
	if resultado.status_code == 200:
		# Se convierte en un JSON la respuesta recibida
		respuesta = resultado.json()
		sentiment = respuesta["label"]

		if sentiment == "neg":
			return "negativo"
		elif sentiment == "pos":
			return "positivo"
		else:
			return "neutral"
	else:
		return "ninguno"

def get_tweets(title):
	tw_positivos=0
	tw_negativos=0
	tw_neutral=0
	totales= {}
	# Obtener todos los tw del titulo o serie para obtener su sentimiento
	tw_keys = r.keys(title+':*:')
	if tw_keys is not None:
		for tw_key in tw_keys:
			# Verificar que no exista el tw en la base de datos
			if(r.exists(tw_key+"sentiment")==0):
				#Enviar el tw analizar para obtener el sentimiento
				sentimiento = get_sentiment_tw(r.get(tw_key))
				#Guardar el sentimiento en la base de datos
				#sentimiento = "positivo"
				r.set(tw_key+"sentiment",sentimiento)
			#Obtener los sentimientos para contabilizarlos de acuerdo a si es
			#positivo, negativo o neutral
			sentimiento_tw = r.get(tw_key+"sentiment")
			if(sentimiento_tw=="positivo"):
			    tw_positivos+=1

			if(sentimiento_tw=="negativo"):
			    tw_negativos+=1

			if(sentimiento_tw=="neutral"):
			    tw_neutral+=1

		totales = {'neutral': tw_neutral,'positivo': tw_positivos,'negativo': tw_negativos}
		sentimiento_pelicula=max(totales, key=totales.get)
		totales['sentimiento_pelicula']=sentimiento_pelicula
		#Enviar respuesta en formato json
		json_totales = json.dumps(totales)

	return json_totales


if __name__ == '__main__':
	# Se define el puerto del sistema operativo que utilizará el servicio
	port = int(os.environ.get('PORT', 8085))
	# Se habilita la opción de 'debug' para visualizar los errores
	app.debug = True
	# Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
	app.run(host='0.0.0.0', port=port)
