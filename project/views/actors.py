# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import connexion
from flask import jsonify

from project.models.init_db import db
from project.models.models import Actor
from project.serializers.serializers import ActorSchema


def get():
    query = Actor.query.paginate(
        connexion.request.args.get("paginationKey", 1),
        connexion.request.args.get("pageSize", 5)
    )
    schema = ActorSchema()
    result = schema.dump(query.items, many=True)
    return jsonify(result), 200


def search():
    return get()


def post():
    if connexion.request.is_json:
        data = connexion.request.get_json()
        actor = Actor(name=data["name"], surname=data["surname"])
        db.session.add(actor)
        db.session.commit()

        return jsonify(ActorSchema().dump(actor))
    return jsonify({})
