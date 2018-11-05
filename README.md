# microservices-scaffold
Barebones Python Microservices

[![Build Status](https://travis-ci.org/python-microservices/microservices-scaffold.svg?branch=master)](https://travis-ci.org/python-microservices/microservices-scaffold)
[![Coverage Status](https://coveralls.io/repos/github/python-microservices/microservices-scaffold/badge.svg?branch=master)](https://coveralls.io/github/python-microservices/microservices-scaffold?branch=master)
[![Requirements Status](https://requires.io/github/python-microservices/microservices-scaffold/requirements.svg?branch=master)](https://requires.io/github/python-microservices/microservices-scaffold/requirements/?branch=master)
[![Updates](https://pyup.io/repos/github/python-microservices/microservices-scaffold/shield.svg)](https://pyup.io/repos/github/python-microservices/microservices-scaffold/)
[![Python 3](https://pyup.io/repos/github/python-microservices/microservices-scaffold/python-3-shield.svg)](https://pyup.io/repos/github/python-microservices/microservices-scaffold/)



# Docker

Create and push the image

    docker build -t template -f Dockerfile .

Test the image:

    docker run -d -p 5000:5000 template
    
    
Push to Kubernetes:

    kubectl apply -f service.yaml
    
    
## How to contrib

TODO

### Update docs

   sphinx-build -b html docs/ _build