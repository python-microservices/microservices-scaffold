import json
import os
import unittest
from typing import Dict, List, Union, Text

from project import MyMicroservice
from pyms.constants import CONFIGMAP_FILE_ENVIRONMENT


def _format_response(response: Text = "") -> Union[List, Dict]:
    # python3.5 compatibility
    if isinstance(response, bytes):
        response = str(response, encoding="utf-8")
    return json.loads(response)


class ProjectTestCase(unittest.TestCase):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def setUp(self):
        os.environ[CONFIGMAP_FILE_ENVIRONMENT] = os.path.join(self.BASE_DIR, "config-tests.yml")
        ms = MyMicroservice(service="ms", path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "project", "test_views.py"))
        self.app = ms.create_app()
        self.base_url = self.app.config["APPLICATION_ROOT"]
        self.client = self.app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(404, response.status_code)

    def test_healthcheck(self):
        response = self.client.get('/healthcheck')
        self.assertEqual(200, response.status_code)

    def test_list_view(self):
        response = self.client.get('{base_url}/'.format(base_url=self.base_url))
        self.assertEqual(200, response.status_code)

    def test_create_view(self):
        name = "blue"
        response = self.client.post('{base_url}/'.format(
            base_url=self.base_url),
            data=json.dumps(dict(name=name)),
            content_type='application/json'
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(name, _format_response(response.data)["name"])

    def tearDown(self):
        pass # os.unlink(self.app.config['DATABASE'])