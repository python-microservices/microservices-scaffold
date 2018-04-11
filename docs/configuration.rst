Configuration
=============

The project is configured in `project/config.py`. You must set the project name `APP_NAME` and the path prefix
of the project `APPLICATION_ROOT`. This constants is defined in the class Config:

.. code-block:: python

    class Config:
        DEBUG = False
        TESTING = False
        APP_NAME = "Template"
        APPLICATION_ROOT = "/template"

Documentation
-------------
The Microservice create a URL to inspect the Swagger documentation of the api in:

.. code-block:: bash
    localhost:5000/[APPLICATION_ROOT]/apidocs/

Our API Rest work with `Flasgger <https://github.com/rochacbruno/flasgger>`_. You can see Flasgger docs or the official
`Swagger documentation <https://swagger.io/specification/>`_ to add the syntax to your APIS and create your Swagger docs