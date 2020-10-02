import json
import os
import pytest
from typing import Dict, List, Union, Text
from pyms.constants import CONFIGMAP_FILE_ENVIRONMENT
from pyms.flask.app import config

from project.app import MyMicroservice

backup_config = config()


def _format_response(response: Text = "") -> Union[List, Dict]:
    # python3.5 compatibility
    if isinstance(response, bytes):
        response = str(response, encoding="utf-8")
    return json.loads(response)


class TestProject:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    @pytest.fixture(scope="session")
    def microservice(self):
        os.environ[CONFIGMAP_FILE_ENVIRONMENT] = os.path.join(self.BASE_DIR, "config-tests.yml")
        ms = MyMicroservice(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "project", "test_views.py"))
        ms.app = ms.create_app()
        ms.base_url = ms.app.config["APPLICATION_ROOT"]
        ms.client = ms.app.test_client()
        return ms

    def test_home(self, microservice):
        response = microservice.client.get('/')
        assert 404 == response.status_code

    def test_healthcheck(self, microservice):
        response = microservice.client.get('/healthcheck')
        assert 200 == response.status_code

    def test_list_actors(self, microservice):
        response = microservice.client.get('/actors'.format(base_url=self.base_url))
        self.assertEqual(200, response.status_code)

    def test_list_films(self, microservice):
        response = microservice.client.get('/films'.format(base_url=self.base_url))
        self.assertEqual(200, response.status_code)

    def test_pyms(self):
        self.assertEqual("1234", self.app.config["TEST_VAR"])

    def test_create_film(self, microservice):
        name = "Avengers"
        pubDate = "2020-01-20"
        cast = [{"id": 1, "name": "Robert", "surname": "Downey Jr."}, {"id": 2, "name": "Chris", "surname": "Hemsworth"}]
        response = microservice.client.post('/films'.format(
            base_url=microservice.base_url),
            data=json.dumps(dict(name=name, pubDate=pubDate, cast=cast)),
            content_type='application/json'
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(name, _format_response(response.data)["name"])

    def test_create_actor(self, microservice):
        response = microservice.client.get('/actors'.format(base_url=microservice.base_url))
        assert 200 == response.status_code

    def test_pyms(self, microservice):
        assert "1234" == microservice.app.config["TEST_VAR"]

    def test_create_view(self, microservice):
        name = "Robert"
        surname = "Downey Jr."
        response = microservice.client.post('/actors'.format(
            base_url=microservice.base_url),
            data=json.dumps(dict(name=name, surname=surname)),
            content_type='application/json'
        )
        assert 200 == response.status_code
        assert name == _format_response(response.data)["name"]