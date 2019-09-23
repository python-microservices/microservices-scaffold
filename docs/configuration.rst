Configuration
=============

Project configuration is loaded using py-ms package based on yml or json file.
Some example files are config.yml, config-docker.yml and tests/config-tests.yml or see `PyMS configuration <https://py-ms.readthedocs.io/en/latest/configuration/>`_

Documentation
-------------
The Microservice create a URL to inspect the Swagger documentation of the api in:

.. code-block:: bash
    localhost:5000/[APPLICATION_ROOT]/ui/

Our API Rest work with `connexion <http://connexion.readthedocs.io>`_. You can see connexion docs or the official
`Swagger documentation <https://swagger.io/specification/>`_ to add the syntax to your APIS and create your Swagger docs