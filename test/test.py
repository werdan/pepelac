import pytest
import requests
from pepelac import pepelac

BASE_URL = 'http://127.0.0.1:65432/'


class TestClass(object):

    server = {}

    def finalizer(self):
        self.server.stop()

    @pytest.fixture(scope="session", autouse=True)
    def setup_server(self):
        self.server = pepelac.Server()
        self.server.start({})
        yield self.finalizer

    def test_get_basedir(self):
        response = requests.get(BASE_URL)
        print(response.status_code)
        print(response.request.headers)
        print(response.headers)
        assert response.content == b'DATA'

    def test_get_second_request(self):
        response = requests.get(BASE_URL)
        print(response.status_code)
        print(response.request.headers)
        print(response.headers)
        assert response.content == b'DATA'
