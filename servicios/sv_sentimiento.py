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
#           +-----------------------+--------------------------+-----------------------------+
#           |  Nombre del elemento  |     Responsabilidad      |      Propiedades            |
#           +-----------------------+--------------------------+-----------------------------+
#           |                       |  - Ofrecer un JSON que   | - Utiliza el API de         |
#           |    Procesador de      |    contenga el sentimien-|   IMDb.                     |
#           |    sentimientos       |    to de los comentarios | - Devuelve un JSON con el   |
#           |    de mashape         |    en tw de películas o  |   sentimiento de la serie o |
#           |                       |    series en particular. |   pelicula en cuestión.     |
#           +-----------------------+--------------------------+-----------------------------+
#
#	Ejemplo de uso: Abrir navegador e ingresar a http://localhost:8085/api/v1/sentimiento?t=matrix
#
import os
from flask import Flask, abort, render_template, request
import urllib, json, requests
import settings
app = Flask (__name__)

@app.route("/api/v1/sentimiento")
def get_analyze():
	# Método que obtiene la información del sentimiento acerca de un título en particular
	# Se lee el parámetro 't' que contiene el título de la película o serie que se va a consultar
	title = request.args.get("t")
	# Se verifica si el parámetro no esta vacío
	if title is not None:
		# Se conecta con el servicio de mashape a través de su API
		endpoint = 'https://text-sentiment.p.mashape.com/analyze'
		headers = {
		'X-Mashape-Key': settings.MASHAPE_KEY,
		"Content-Type": "application/x-www-form-urlencoded",
		"Accept": "application/json"
		}
        # Se envían los paramétros al API
		params = {
		'language': 'english',
		'text': title,
		}

		# Se obtiene la respuesta de mashape
		resultado = requests.post(endpoint, headers=headers, params=params)
		# {"lang": "ENGLISH", "totalLines": 1, "text": "I am not really happy", "mid_percent": "0%", "mid": 0, "pos": 0, "pos_percent": "0%", "neg": 1, "neg_percent": "100%"}
        # Se convierte en un JSON la respuesta recibida
		respuesta = resultado.json()
		# Se regresa el JSON de la respuesta
		return json.dumps(respuesta)
 	else:
 		# Se devuelve un error 400 para indicar que el servicio no puede funcionar sin parámetro
 		abort(400)



if __name__ == '__main__':
	# Se define el puerto del sistema operativo que utilizará el servicio
	port = int(os.environ.get('PORT', 8085))
	# Se habilita la opción de 'debug' para visualizar los errores
	app.debug = True
	# Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
	app.run(host='0.0.0.0', port=port)