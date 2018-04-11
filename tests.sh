#!/bin/sh
coverage erase
tox
coverage combine
coverage report -m
coverage html
pylint project/* > pylintReport.txt