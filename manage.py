# encoding: utf-8
from project.app import MyMicroservice


def create_app():
    """Initialize the Flask app, register blueprints and intialize all libraries like Swagger, database, the trace system...
    return the app and the database objects.
    :return:
    """
    ms = MyMicroservice(path=__file__)
    return ms.create_app()


app = create_app()

if __name__ == '__main__':
    app.run()
