# -*- coding: utf-8 -*-
from twython import Twython
from slugify import slugify
import json
import redis
import settings
import os
from flask import Flask, abort, render_template, request
import urllib, json
import sys
app = Flask (__name__)


APP_KEY = 'MUebLOiElmDhgGoyFYZelhiMn'
APP_SECRET = 'eSJBb3LYEuN7XFV5U00IFBNtuWBgmsHPeUfPk8HkSxaIhTvMgR'
OAUTH_TOKEN = '2891574093-0FgmSMcryoJXoCOObTSneUALpRTSpqpo53WDuRj'
OAUTH_TOKEN_SECRET = 'QwC7VGrYjH9jo0eBKlR8cK8bHv6cUwLIzNzFKN4khfM5G'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

@app.route("/api/v1/tweets")
def get_tweets():
    title = request.args.get("t")
    title = slugify(title)
    
    resultados = twitter.search(q=title, count=50)
    datos = resultados.keys()
    for i in range(len(resultados[datos[1]])):
        id_title = resultados[datos[1]][i][u'id_str']
        text = resultados[datos[1]][i][u'text']
        r.set(title+":"+id_title,text)
    return title
            

if __name__ == '__main__':

	port = int(os.environ.get('PORT', 8086))
	app.debug = True
	app.run(host='0.0.0.0', port=port)