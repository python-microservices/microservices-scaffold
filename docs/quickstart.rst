Quickstart
==========

Scaffold
--------

Clone the project

.. code-block:: bash

    git clone https://github.com/python-microservices/microservices-scaffold.git

Install your virtualenv

.. code-block:: bash

    virtualenv --python=python[3.6|3.7|3.8] venv
    source venv/bin/activate
    pip install -r requirements.txt

Run the script

.. code-block:: bash

    python manage.py runserver

*Check the result*

Your default endpoint will be in this url:

.. code-block:: bash

    http://127.0.0.1:5000/template/


This URL is setted in your `config.yml`:

.. code-block:: yaml

    pyms:
      config:
        DEBUG: false
        TESTING: false
        APP_NAME: Template
        APPLICATION_ROOT : /template # <!---

You can acceded to a `swagger ui <https://swagger.io/tools/swagger-ui/>`_ in the next url:

.. code-block:: bash
    http://127.0.0.1:5000/template/ui/


This PATH is setted in your `config.yml`:

.. code-block:: yaml
    pyms:
      services:
        swagger:
          path: "swagger"
          file: "swagger.yaml"
          url: "/ui/" # <!---

Template
--------

You can create your own project from template:

https://github.com/python-microservices/microservices-template