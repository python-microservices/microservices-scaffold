# microservices-scaffold

![Python package](https://github.com/python-microservices/microservices-scaffold/workflows/Python%20package/badge.svg?branch=master)
[![Build Status](https://travis-ci.org/python-microservices/microservices-scaffold.svg?branch=master)](https://travis-ci.org/python-microservices/microservices-scaffold)
[![Coverage Status](https://coveralls.io/repos/github/python-microservices/microservices-scaffold/badge.svg?branch=master)](https://coveralls.io/github/python-microservices/microservices-scaffold?branch=master)
[![Requirements Status](https://requires.io/github/python-microservices/microservices-scaffold/requirements.svg?branch=master)](https://requires.io/github/python-microservices/microservices-scaffold/requirements/?branch=master)
[![Updates](https://pyup.io/repos/github/python-microservices/microservices-scaffold/shield.svg)](https://pyup.io/repos/github/python-microservices/microservices-scaffold/)
[![Python 3](https://pyup.io/repos/github/python-microservices/microservices-scaffold/python-3-shield.svg)](https://pyup.io/repos/github/python-microservices/microservices-scaffold/)

Python Microservice Scaffold is an example of how to structure a Flask Microservice Project.
This Scaffold is build over [PyMS](https://github.com/python-microservices/pyms) package. PyMS is a 
[Microservice chassis pattern](https://microservices.io/patterns/microservice-chassis.html)
like Spring Boot (Java) or Gizmo (Golang). PyMS is a collection of libraries, best practices and recommended ways to build
microservices with Python which handles cross-cutting concerns:
- Externalized configuration
- Logging
- Health checks
- Metrics
- Distributed tracing

## Quickstart

We recommended use [Poetry](https://python-poetry.org/docs/) to install the dependencies

Start with poetry
```shell
pip install --user poetry
poetry update
poetry run python manage.py
```

Start with a virtualenv
```shell
pip install -r requirements.txt
python manage.py
```


Open `http://127.0.0.1:5000/ui/` and play with swagger

See our [quickstart webpage](https://python-microservices.github.io/scaffold/quickstart/)

# Dependencies

Updated dependencies in a requirements.txt with:

```shell
poetry export --dev -f requirements.txt --output requirements.txt
```

# How To contribute

We appreciate opening issues and pull requests to make PyMS even more stable & useful! See [This doc](CONTRIBUTING.md)
for more details