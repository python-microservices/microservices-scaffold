# encoding: utf-8
from flask_script import Manager

from project.app import MyMicroservice


def create_app():
    """Initialize the Flask app, register blueprints and intialize all libraries like Swagger, database, the trace system...
    return the app and the database objects.
    :return:
    """
    ms = MyMicroservice(path=__file__)
    return ms.create_app()


app = create_app()

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
