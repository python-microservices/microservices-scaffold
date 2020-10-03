import json
from typing import Dict, List, Union, Text

from pyms.flask.app import config

backup_config = config()


def _format_response(response: Text = "") -> Union[List, Dict]:
    # python3.5 compatibility
    if isinstance(response, bytes):
        response = str(response, encoding="utf-8")
    return json.loads(response)


def test_home(client):
    response = client.get('/')
    assert 404 == response.status_code


def test_healthcheck(client):
    response = client.get('/healthcheck')
    assert 200 == response.status_code


def test_list_actors(client, base_url):
    response = client.get('{base_url}actors'.format(base_url=base_url))
    assert 200 == response.status_code


def test_list_films(client, base_url):
    response = client.get('{base_url}films'.format(base_url=base_url))
    assert 200 == response.status_code


def test_pyms(app):
    assert "1234" == app.config["TEST_VAR"]


def test_create_film(client, base_url):
    name = "Avengers"
    pubDate = "2020-01-20"
    cast = [{"id": 1, "name": "Robert", "surname": "Downey Jr."}, {"id": 2, "name": "Chris", "surname": "Hemsworth"}]
    response = client.post('{base_url}films'.format(
        base_url=base_url),
        data=json.dumps(dict(name=name, pubDate=pubDate, cast=cast)),
        content_type='application/json'
    )
    assert 200 == response.status_code
    assert name == _format_response(response.data)["name"]


def test_create_view(client, base_url):
    name = "Robert"
    surname = "Downey Jr."
    response = client.post('{base_url}actors'.format(
        base_url=base_url),
        data=json.dumps(dict(name=name, surname=surname)),
        content_type='application/json'
    )
    assert 200 == response.status_code
    assert name == _format_response(response.data)["name"]
