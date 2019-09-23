.. Python Microservices documentation master file, created by
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python Microservices
====================
Python Microservice Scaffold is an example to how structure a Flask Microservice Project.
This Scaffold is build over `PyMS <https://github.com/python-microservices/pyms>`_ package. PyMS is a `Microservice chassis pattern <https://microservices.io/patterns/microservice-chassis.html>`_
like Spring Boot (Java) or Gizmo (Golang). PyMS is a collection of libraries, best practices and recommended ways to build
microservices with Python which handles cross-cutting concerns:
- Externalized configuration
- Logging
- Health checks
- Metrics (TODO)
- Distributed tracing


Stack
-----
* `PyMS <https://github.com/python-microservices/pyms>`_
* `connexion <http://connexion.readthedocs.io>`_
* `Flask <https://github.com/pallets/flask>`_
* `SQLAlchemy <https://www.sqlalchemy.org/>`_
* `Flask-SQLAlchemy <http://flask-sqlalchemy.pocoo.org/2.3/>`_
* `Flask-Injector <https://github.com/alecthomas/flask_injector>`_
* `Flask-Script <https://flask-script.readthedocs.io/en/latest/>`_
* `Opentracing <https://github.com/opentracing-contrib/python-flask>`_


Content
-------
.. toctree::
   :maxdepth: 4

   installation
   runinkubernetes
   quickstart
   structure
   configuration
   codeexample
   project
