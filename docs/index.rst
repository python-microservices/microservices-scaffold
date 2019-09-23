.. Python Microservices documentation master file, created by
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python Microservices
====================
Python Microservice Scaffold is an example to how structure a Flask Microservice Project.
This Scaffold is build over `PyMS <https://github.com/python-microservices/pyms>`_ package. PyMS is a `Microservice chassis pattern <https://microservices.io/patterns/microservice-chassis.html>`_
like Spring Boot (Java) or Gizmo (Golang). PyMS is a collection of libraries, best practices and recommended ways to build
microservices with Python which handles cross-cutting concerns:

* Externalized configuration
* Logging
* Health checks
* Metrics (TODO)
* Distributed tracing


Stack
-----
* `PyMS <https://github.com/python-microservices/pyms>`_
   * `Flask <https://github.com/pallets/flask>`_
   * `connexion <http://connexion.readthedocs.io>`_
   * `Opentracing <https://github.com/opentracing-contrib/python-flask>`_
* `SQLAlchemy <https://www.sqlalchemy.org/>`_
* `Flask-SQLAlchemy <http://flask-sqlalchemy.pocoo.org/2.3/>`_
* `Flask-Script <https://flask-script.readthedocs.io/en/latest/>`_



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
