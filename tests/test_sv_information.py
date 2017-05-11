import json
import urllib
import httpretty
from servicios.sv_information import app


class TestInformationService:

    def setup(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    @httpretty.activate
    def test_get_information(self):
        httpretty.register_uri(
            httpretty.GET,
            'http://www.omdbapi.com',
            body="""
            {
                "Title": "Drive Me Crazy",
                "Director": "John Schultz",
                "Type": "movie"
            }
            """,
            content_type='application/json')

        data = {'t': 'Drive me crazy'}

        response = self.client.get(
            '/api/v1/information?' + urllib.urlencode(data))
        data = json.loads(response.data)

        assert response.status_code == 200
        assert 'Type' in data

    def test_get_information_bad_request(self):
        response = self.client.get('/api/v1/information')

        assert response.status_code == 400
