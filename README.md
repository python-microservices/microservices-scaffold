# microservices-scaffold
Python Microservice Scaffold is an example of how to structure a Flask Microservice Project.
This Scaffold is build over [PyMS](https://github.com/python-microservices/pyms) package. PyMS is a [Microservice chassis pattern](https://microservices.io/patterns/microservice-chassis.html)
like Spring Boot (Java) or Gizmo (Golang). PyMS is a collection of libraries, best practices and recommended ways to build
microservices with Python which handles cross-cutting concerns:
- Externalized configuration
- Logging
- Health checks
- Metrics
- Distributed tracing

[![Build Status](https://travis-ci.org/python-microservices/microservices-scaffold.svg?branch=master)](https://travis-ci.org/python-microservices/microservices-scaffold)
[![Coverage Status](https://coveralls.io/repos/github/python-microservices/microservices-scaffold/badge.svg?branch=master)](https://coveralls.io/github/python-microservices/microservices-scaffold?branch=master)
[![Requirements Status](https://requires.io/github/python-microservices/microservices-scaffold/requirements.svg?branch=master)](https://requires.io/github/python-microservices/microservices-scaffold/requirements/?branch=master)
[![Updates](https://pyup.io/repos/github/python-microservices/microservices-scaffold/shield.svg)](https://pyup.io/repos/github/python-microservices/microservices-scaffold/)
[![Python 3](https://pyup.io/repos/github/python-microservices/microservices-scaffold/python-3-shield.svg)](https://pyup.io/repos/github/python-microservices/microservices-scaffold/)

Table of Contents
=================

   * [microservices-scaffold](#microservices-scaffold)
   * [How to run the scaffold](#how-to-run-the-scaffold)
      * [Installation](#installation)
         * [Clone the repository](#clone-the-repository)
         * [Install with virtualenv](#install-with-virtualenv)
         * [Install with pipenv](#install-with-pipenv)
            * [Advantages over plain pip and requirements.txt](#advantages-over-plain-pip-and-requirementstxt)
      * [Run your python script](#run-your-python-script)
      * [Check the result](#check-the-result)
   * [Docker](#docker)
   * [Kubernetes](#kubernetes)
  * [How To contribute](#how-to-contribute)
         
# How to run the scaffold

## Installation

### Clone the repository

```bash
git clone git@github.com:purwowd/microservices-scaffold.git
cd microservices-scaffold
```

### Install with virtualenv
```bash
virtualenv --python=python[3.6|3.7|3.8] venv
source venv/bin/activate
pip install -r requirements.txt
```

### Install with pipenv
```bash
pip install pipenv
pipenv install
```

### Install on MacOS
```bash
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
python manage.py runserver
```

#### Advantages over plain pip and requirements.txt
[Pipenv](https://pipenv.readthedocs.io/en/latest/) generates two files: a `Pipfile`and a `Pipfile.lock`.
* `Pipfile`: Is a high level declaration of the dependencies of your project. It can contain "dev" dependencies (usually test related stuff) and "standard" dependencies which are the ones you'll need for your project to function
* `Pipfile.lock`: Is the "list" of all the dependencies your Pipfile has installed, along with their version and their hashes. This prevents two things: Conflicts between dependencies and installing a malicious module.

For a more in-depth explanation please refer to  the [official documentation](https://pipenv.readthedocs.io/en/latest/).

## Run your python script
```bash
python manage.py runserver
```


## Check the result

Your default endpoints will be in this url:
```bash
http://127.0.0.1:5000/films
http://127.0.0.1:5000/actors
```

This URL is set in your `config.yml`:

```yaml
pyms:
  config:
    DEBUG: false
    TESTING: false
    APP_NAME: Template
    APPLICATION_ROOT : "" # <!---
```

You can acceded to a [swagger ui](https://swagger.io/tools/swagger-ui/) in the next url:
```bash
http://127.0.0.1:5000/ui/
```

This PATH is set in your `config.yml`:

```yaml
pyms:
  services:
    swagger:
      path: "swagger"
      file: "swagger.yaml"
      url: "/ui/" # <!---
```

Read more info in the documentation page: 
https://microservices-scaffold.readthedocs.io/en/latest/

# Docker
You can dockerize this microservice with these steps:
* Create and push the image

    docker build -t films -f Dockerfile .
* Run the image:

    docker run -d -p 5000:5000 films
    
 
# Kubernetes
You can run this microservice in a Kubernetes cluster with:

    kubectl apply -f service.yaml

# How To contribute

We appreciate opening issues and pull requests to make PyMS even more stable & useful! See [This doc](CONTRIBUTING.md)
for more details