# -*- coding: utf-8 -*-
from twython import Twython
from twython import TwythonStreamer
import json
import os
from flask import Flask, abort, render_template, request
import urllib, json
import sys
app = Flask (__name__)
#from flask import title

@app.route("/api/v1/tweets")
def get_tweet():
    title = request.args.get("t")
    
    APP_KEY = 'MUebLOiElmDhgGoyFYZelhiMn'
    APP_SECRET = 'eSJBb3LYEuN7XFV5U00IFBNtuWBgmsHPeUfPk8HkSxaIhTvMgR'
    OAUTH_TOKEN = '2891574093-0FgmSMcryoJXoCOObTSneUALpRTSpqpo53WDuRj'
    OAUTH_TOKEN_SECRET = 'QwC7VGrYjH9jo0eBKlR8cK8bHv6cUwLIzNzFKN4khfM5G'
    
    
    stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=title)

@app.route("/api/v1/tweets")
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        title = request.args.get("t")
        with open(title + '.json', 'a') as f:
            f.write(json.dumps(data[u'text'])+"\n")
            # Para abrir después.
            #json_read = json_tweets.read()
            #tweet = json.loads(json_read)
            #return json.dumps(tweet)
        


if __name__ == '__main__':

	port = int(os.environ.get('PORT', 8086))
	app.debug = True
	app.run(host='0.0.0.0', port=port)