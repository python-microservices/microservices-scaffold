#!/bin/sh
pip install -r requirements-tests.txt
coverage erase
coverage run -m unittest
coverage combine
coverage report -m
coverage xml -i
coverage html -i
# --rcfile=pylintrc
pylint project/* > pylintReport.txt