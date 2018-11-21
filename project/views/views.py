# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals
from sys import exc_info

import connexion
from flask import jsonify, current_app

from project.models.init_db import db
from project.models.models import Colors


def list_view():
    """Example endpoint return a list of colors by palette
    """
    try:
        current_app.logger.info("Return all color list")
        query = Colors.query.all()
        return jsonify([i.serialize for i in query])
    except Exception as e:
        exc_error_type, exc_value, exc_traceback = exc_info()
        current_app.logger.error(
            "Error: {}, type: {},  traceback: {}".format(e, exc_error_type, exc_traceback),
            exc_info=exc_traceback
        )


def create_view():
    """Example endpoint return create a color
    """
    # import ipdb; ipdb.set_trace()
    current_app.logger.info("Create color")

    if connexion.request.is_json:
        data = connexion.request.get_json()
        color = Colors(name=data["name"])
        db.session.add(color)
        db.session.commit()

        return jsonify(color.serialize)
    return jsonify({})
