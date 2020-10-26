import os

import pytest

from manage import create_app
from project.models.init_db import db as _db


def conf_environment():
    if not os.environ.get("PYMS_CONFIGMAP_FILE", False):
        os.environ["PYMS_CONFIGMAP_FILE"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config-tests.yml")


@pytest.fixture(scope="session")
def app():
    conf_environment()
    app = create_app()
    return app


@pytest.fixture(scope="module")
def client(app, db):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture(scope="module")
def base_url(app):
    """Base url of the service."""
    return app.config["APPLICATION_ROOT"]


@pytest.fixture(scope="session")
def db(app, request):
    def teardown():
        _db.drop_all()

    _db.app = app
    _db.init_app(app)
    _db.create_all()

    request.addfinalizer(teardown)

    return _db


@pytest.fixture(scope="session")
def db_handler(app_handler, request):
    def teardown():
        _db.drop_all()

    _db.app = app_handler
    _db.init_app(app_handler)
    _db.create_all()

    request.addfinalizer(teardown)

    return _db
