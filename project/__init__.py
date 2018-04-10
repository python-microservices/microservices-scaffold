# encoding: utf-8

import os

from flasgger import Swagger
from flask import Flask

from project.config import CONFIG

__author__ = "Alberto Vara"
__email__ = "a.vara.1986@gmail.com"
__version__ = "0.0.1"

ENVIRONMENT = os.environ.get("ENVIRONMENT", "default")

SWAGGER_CONFIG = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '{application_root}/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "info": {
        "title": "API ",
        "description": "API para...",
        "contact": {
            "responsibleOrganization": "ME",
            "responsibleDeveloper": "Me",
            "email": "me@me.com",
        },
        "version": "0.0.1"
    },
    "securityDefinitions": {
        "APIKeyHeader": {"type": "apiKey", "name": "Authorization", "in": "header"},
    },
    "static_url_path": "{application_root}/flasgger_static",
    "swagger_ui": True,
    "uiversion": 2,
    "specs_route": "/apidocs/",
    "basePath": "{application_root}"
}


class PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        elif environ['PATH_INFO'].startswith("/healthcheck"):
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]


def create_app():
    from project.models import db
    from project.views import views_bp as views_blueprint
    from project.views import views_hc as views_hc_blueprint
    environment = os.environ.get("ENVIRONMENT", "default")

    app = Flask(__name__)
    app.config.from_object(CONFIG[environment])
    app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix=app.config["APPLICATION_ROOT"])

    db.init_app(app)

    SWAGGER_CONFIG["specs"][0]["route"] = SWAGGER_CONFIG["specs"][0]["route"].format(
        application_root=app.config["APPLICATION_ROOT"]
    )
    SWAGGER_CONFIG["static_url_path"] = SWAGGER_CONFIG["static_url_path"].format(
        application_root=app.config["APPLICATION_ROOT"]
    )
    SWAGGER_CONFIG["specs_route"] = SWAGGER_CONFIG["specs_route"].format(
        application_root=app.config["APPLICATION_ROOT"]
    )
    SWAGGER_CONFIG["basePath"] = SWAGGER_CONFIG["basePath"].format(
        application_root=app.config["APPLICATION_ROOT"]
    )
    Swagger(app, config=SWAGGER_CONFIG)

    app.register_blueprint(views_blueprint)
    app.register_blueprint(views_hc_blueprint)
    with app.test_request_context():
        db.create_all()
    return app, db
