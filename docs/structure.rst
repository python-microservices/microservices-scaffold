Structure
=========

You have a project with this structure:

.. code-block:: bash

   Dockerfile
   LICENSE
   manage.py
   config.yml
   README.md
   requirements.txt
   requirements-tests.txt
   requirements-docker.txt
   service.yaml
   setup.py
   Makefile
   tox.ini
   project
   ├ __init__.py
   ├ models
   │ ├ __init__.py
   │ └ models.py
   ├ swagger
   │ └ swagger.yaml
   ├ tests
   │ └ test_views.py
   └views
     ├ __init__.py
     └ views.py
   docs/
   tests/


manager.py
----------

A Django style command line. Use this to start the application like:

.. code-block:: bash

    python manage.py runserver

You can set the host and the port with:

.. code-block:: bash

    python manage.py runserver -h 0.0.0.0 -p 8080


Common Libraries
----------------

py-ms is a library that contains a set of common features for microservices.

Structure of a project
----------------------

For project configuration see :doc:`configuration </configuration>` section.

project/models/init_db.py
~~~~~~~~~~~~~~~~~~~~~~~~~
Initialize `flask_sqlalchemy.SQLAlchemy object`.

project/models/models.py
~~~~~~~~~~~~~~~~~~~~~~~~
Project specific models.

project/swagger/swagger.yaml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Use to define your rest behaviour, endpoints and routes. See `connexion <http://connexion.readthedocs.io>`_ docs to how add new views.

project/views
~~~~~~~~~~~~~
use views.py or create your file.

project/__init__.py
~~~~~~~~~~~~~~~~~~~
This file init the project calling `create_app` method. Initialize the Flask app, register `blueprints <http://flask.pocoo.org/docs/0.12/blueprints/>`_
and initialize all libraries like Swagger, database, trace system, custom logger format, etc.

