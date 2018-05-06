# encoding: utf-8

import logging
import os

import connexion
from flask_injector import FlaskInjector
from injector import Injector

from project.config import CONFIG
from pyms.healthcheck import healthcheck_blueprint
from pyms.logger import CustomJsonFormatter
from pyms.models import db
from pyms.tracer.main import TracerModule

__author__ = "Alberto Vara"
__email__ = "a.vara.1986@gmail.com"
__version__ = "0.2"

logger = logging.getLogger('jaeger_tracing')
logger.setLevel(logging.DEBUG)

ENVIRONMENT = os.environ.get("ENVIRONMENT", "default")


def create_app():
    """Initialize the Flask app, register blueprints and intialize all libraries like Swagger, database, the trace system...
    return the app and the database objects.
    :return:
    """
    environment = os.environ.get("ENVIRONMENT", "default")

    app = connexion.App(__name__, specification_dir='./swagger/')
    # app.app.json_encoder = encoder.JSONEncoder

    app.add_api('swagger.yaml',
                arguments={'title': 'Swagger Example Project'},
                base_path=CONFIG[environment].APPLICATION_ROOT)

    application = app.app
    application.config.from_object(CONFIG[environment])
    db.init_app(application)

    # Initialize Blueprints
    application.register_blueprint(healthcheck_blueprint)

    # Inject Modules
    if not application.config["TESTING"] and not application.config["DEBUG"]:
        log_handler = logging.StreamHandler()
        formatter = CustomJsonFormatter('(timestamp) (level) (name) (module) (funcName) (lineno) (message)')
        formatter.add_service_name(application.config["APP_NAME"])
        tracer = TracerModule(application)
        injector = Injector([tracer])
        FlaskInjector(app=application, injector=injector)
        formatter.add_trace_span(tracer.tracer)
        log_handler.setFormatter(formatter)
        application.logger.addHandler(log_handler)
        application.logger.setLevel(logging.INFO)

    with application.test_request_context():
        db.create_all()

    return application, db
