from servicios.sv_tweets import app
import httpretty


class TestSentimientoService:

    def setup(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_get_analyze_bad_request(self):
        response = self.client.get('/api/v1/tweets')

        assert response.status_code == 400
