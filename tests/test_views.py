import json
import os
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

    def setup_method(self):
        os.environ[CONFIGMAP_FILE_ENVIRONMENT] = os.path.join(self.BASE_DIR, "config-tests.yml")
        ms = MyMicroservice(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "project", "test_views.py"))
        self.app = ms.create_app()
        self.base_url = self.app.config["APPLICATION_ROOT"]
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_home(self):
        response = self.client.get('/')
        assert 404 == response.status_code

    def test_healthcheck(self):
        response = self.client.get('/healthcheck')
        assert 200 == response.status_code

    def test_list_view(self):
        response = self.client.get('/actors'.format(base_url=self.base_url))
        assert 200 == response.status_code

    def test_pyms(self):
        assert "1234" == self.app.config["TEST_VAR"]

    def test_create_view(self):
        name = "Robert"
        surname = "Downey Jr."
        response = self.client.post('/actors'.format(
            base_url=self.base_url),
            data=json.dumps(dict(name=name, surname=surname)),
            content_type='application/json'
        )
        assert 200 == response.status_code
        assert name == _format_response(response.data)["name"]

