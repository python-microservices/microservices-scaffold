# microservices-scaffold
Barebones Python Microservices

[![Build Status](https://travis-ci.org/python-microservices/microservices-scaffold.svg?branch=master)](https://travis-ci.org/python-microservices/microservices-scaffold)
[![Build Status](https://coveralls.io/repos/github/python-microservices/microservices-scaffold/Badge.svg?branch=master)](https://coveralls.io/repos/github/python-microservices/microservices-scaffold)
[![Build Status](https://requires.io/github/python-microservices/microservices-scaffold/requirements.svg?branch=master)](https://requires.io/github/python-microservices/microservices-scaffold/requirements/?branch=master)



# Docker

Create and push the image

    docker build -t template -f Dockerfile .

Test the image:

    docker run -d -p 5000:5000 template
    
    
Push to Kubernetes:

    kubectl create -f service.yaml