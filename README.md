# microservices-scaffold
Barebones Python Microservices

[![Build Status](https://travis-ci.org/python-microservices/microservices-scaffold.svg?branch=master)](https://travis-ci.org/python-microservices/microservices-scaffold)
[![Coverage Status](https://coveralls.io/repos/github/python-microservices/microservices-scaffold/badge.svg?branch=master)](https://coveralls.io/github/python-microservices/microservices-scaffold?branch=master)
[![Requirements Status](https://requires.io/github/python-microservices/microservices-scaffold/requirements.svg?branch=master)](https://requires.io/github/python-microservices/microservices-scaffold/requirements/?branch=master)



# Docker

Create and push the image

    docker build -t template -f Dockerfile .

Test the image:

    docker run -d -p 5000:5000 template
    
    
Push to Kubernetes:

    kubectl create -f service.yaml