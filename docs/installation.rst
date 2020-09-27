Installation
============

Clone the project

.. code-block:: bash

    git clone https://github.com/python-microservices/microservices-scaffold.git

Install your virtualenv

.. code-block:: bash

    virtualenv --python=python[3.6|3.7|3.8] venv
    source venv/bin/activate
    pip install -r requirements.txt

Or innstall with pipenv

.. code-block:: bash

    pip install pipenv
    pipenv install


Advantages over plain pip and requirements.txt
----------------------------------------------

Pipenv generates two files: a `Pipfile` and a `Pipfile.lock`.

* `Pipfile`: Is a high level declaration of the dependencies of your project. It can contain "dev" dependencies
(usually test related stuff) and "standard" dependencies which are the ones you'll need for your project to function
* `Pipfile.lock`: Is the "list" of all the dependencies your Pipfile has installed, along with their version and
their hashes. This prevents two things: Conflicts between dependencies and installing a malicious module.


Configure your project and the path of your MS. See :doc:`configuration </configuration>` section.

Configure your setup.py with your project information