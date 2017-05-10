import urllib
import json
from servicios.sv_information import app


class TestInformationService:

    def setup(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_get_information(self):
        data = {'t': 'The avengers'}

        response = self.client.get(
            '/api/v1/information?' + urllib.urlencode(data))
        data = json.loads(response.data)

        assert response.status_code == 200
        assert 'Type' in data

    def test_get_information_bad_request(self):
        response = self.client.get('/api/v1/information')

        assert response.status_code == 400
