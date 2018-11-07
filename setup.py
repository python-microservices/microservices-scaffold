# -*- coding: utf-8 -*-
# Copyright (c) 2018 by Alberto Vara <a.vara.1986@gmail.com>
import codecs
import os

from setuptools import setup, find_packages

version = __import__('project').__version__
author = __import__('project').__author__
author_email = __import__('project').__email__

if os.path.exists('README.rst'):
    long_description = codecs.open('README.rst', 'r', 'utf-8').read()
else:
    long_description = 'https://github.com/python-microservices/microservices-scaffold'

setup(
    name="MS-Scaffold",
    version=version,
    author=author,
    author_email=author_email,
    description="Python Miscroservice barebone",
    long_description=long_description,
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    python_requires='>=3.5',
    license="GPLv3",
    platforms=["any"],
    keywords="python, microservices",
    url='https://github.com/python-microservices/microservices-scaffold',
    test_suite='nose.collector',
    packages=find_packages(),
    include_package_data=True,
)