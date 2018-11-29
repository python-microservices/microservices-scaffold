from pyms.flask.app import Microservice

from project.models.init_db import db

__author__ = "Alberto Vara"
__email__ = "a.vara.1986@gmail.com"
__version__ = "0.3.1"


class MyMicroservice(Microservice):
    def init_libs(self):
        db.init_app(self.application)
        with self.application.test_request_context():
            db.create_all()


def create_app():
    """Initialize the Flask app, register blueprints and intialize all libraries like Swagger, database, the trace system...
    return the app and the database objects.
    :return:
    """
    ms = MyMicroservice(service="ms", path=__file__)
    return ms.create_app()
