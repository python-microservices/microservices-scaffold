Structure
=========

You have a project with this structure:

.. code-block:: bash

   manager.py
   project
   ├ __init__.py
   ├ config.py
   ├ views
   │ ├ __init__.py
   │ ├ views.py
   │ └ healthcheck.py
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

project/__init__.py
-------------------
This file init the project with the funcion `create_app`. Initialize the Flask app, register `blueprints <http://flask.pocoo.org/docs/0.12/blueprints/>`_
and intialize all libraries like Swagger, database, the trace system...

project/config.py
-----------------
See :doc:`configuration </configuration>` section

project/views
-------------
use views.py or create your file. You must add after register the view blueprint in `project/views/__init__.py`.

project/views/healthcheck.py
----------------------------
This views is usually used by Kubernetes, Eureka and other systems to check if our application is up and running
