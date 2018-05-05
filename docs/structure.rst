Structure
=========

You have a project with this structure:

.. code-block:: bash

   manager.py
   requirements.txt
   requirements-tests.txt
   requirements-docker.txt
   setup.py
   tox.ini
   myms
   ├ healthcheck
   │ └ healthcheck.py
   ├ logger
   │ └ logger.py
   ├ models
   │ └ __init__.py
   └ tracer
     └ main.py
   project
   ├ __init__.py
   ├ config.py
   ├ views
   │ ├ __init__.py
   │ └ views.py
   ├ models
   │ ├ __init__.py
   │ └ models.py
   └ tests
     └ test_views.py

manager.py
----------

A Django style command line. Use this to start the application like:

.. code-block:: bash

    python manage.py runserver

You can set the host and the port with:

.. code-block:: bash

    python manage.py runserver -h 0.0.0.0 -p 8080

Common Structure
----------------

myms/healthcheck/healthcheck.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This views is usually used by Kubernetes, Eureka and other systems to check if our application is up and running

myms/logger/logger.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Print logger in JSON format to send to server like Elasticsearch. Inject span traces in logger

myms/models/__init__.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Initizalize `flask_sqlalchemy.SQLAlchemy object`

myms/tracer/main.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create an injector `flask_opentracing.FlaskTracer` to use in our projects

Structure of a project
----------------------

project/__init__.py
~~~~~~~~~~~~~~~~~~~
This file init the project with the funcion `create_app`. Initialize the Flask app, register `blueprints <http://flask.pocoo.org/docs/0.12/blueprints/>`_
and intialize all libraries like Swagger, database, the trace system...

project/config.py
~~~~~~~~~~~~~~~~~
See :doc:`configuration </configuration>` section

project/views
~~~~~~~~~~~~~
use views.py or create your file. You must add after register the view blueprint in `project/views/__init__.py`.


