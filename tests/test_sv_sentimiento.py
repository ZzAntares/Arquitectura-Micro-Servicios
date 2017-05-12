import json
import urllib
from servicios.sv_sentimiento import app, get_sentiment_tw


import httpretty


class TestSentimientoService:

    def setup(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    @httpretty.activate
    def test_get_sentiment(self):
        httpretty.register_uri(
            httpretty.POST,
            'http://text-processing.com/api/sentiment/',
            body="""
            {
                "label": "neg",
                "probability": {
                    "neg": 0.5260158874169073,
                    "neutral": 0.11228576144941622,
                    "pos": 0.4739841125830927
                }
            }
            """,
            content_type='application/json')

        sentiment = get_sentiment_tw('the-avengers')

        assert sentiment == 'negativo'

    def test_get_analyze_bad_request(self):
        response = self.client.get('/api/v1/sentimiento')

        assert response.status_code == 400
