import json
import urllib
from servicios.sv_sentimiento import app


import httpretty


class TestSentimientoService:

    def setup(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    @httpretty.activate
    def test_get_analyze(self):
        httpretty.register_uri(
            httpretty.GET,
            'https://text-sentiment.p.mashape.com/analyze',
            body="""
            {
                "lang": "ENGLISH",
                "totalLines": 1,
                "text": "It was great I'll watch it again no joke haha",
                "mid_percent": "0%",
                "mid": 0,
                "pos": 1,
                "pos_percent": "100%",
                "neg": 0,
                "neg_percent": "0%"
            }
            """,
            content_type='application/json')

        data = {'t': 'The avengers'}

        response = self.client.get(
            '/api/v1/sentimiento?' + urllib.urlencode(data))

        data = json.loads(response.data)

        assert 'sent' in data
        assert data['sent'] == 'positivo'

    def test_get_analyze_bad_request(self):
        response = self.client.get('/api/v1/sentimiento')

        assert response.status_code == 400
