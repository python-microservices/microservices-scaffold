# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import connexion
from flask import jsonify, current_app

from project.models.init_db import db
from project.models.models import Color
from project.serializers.serializers import ColorSchema


def list_view():
    """Example endpoint return a list of colors by palette
    """
    current_app.logger.info("Return all color list")
    query = Color.query.paginate(
        connexion.request.args.get("paginationKey", 1),
        connexion.request.args.get("pageSize", 5)
    )
    schema = ColorSchema()
    result = schema.dump(query.items, many=True)
    return jsonify(result), 200


def create_view():
    """Example endpoint return create a color
    """
    current_app.logger.info("Create color")
    if connexion.request.is_json:
        data = connexion.request.get_json()
        color = Color(name=data["name"])
        db.session.add(color)
        db.session.commit()

        return jsonify(ColorSchema().dump(color))
    return jsonify({})
