# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

from flask import request, jsonify

from project.models.models import db, Colors
from project.views import views_bp


@views_bp.route('/', methods=['GET'])
def list_view():
    """Example endpoint return a list of colors by palette
    ---
    tags:
      - colors
    operationId: get_colors
    consumes:
      - application/json
    produces:
      - application/json
    schemes: ['http']
    deprecated: false
    externalDocs:
      description: Project repository
      url: http://github.com/rochacbruno/flasgger
    definitions:
      Color:
        type: object
        properties:
          id:
            type: string
          timestamp:
            type: datetime
          name:
            type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Color'
        examples:
          [{
            "id": "2c951676-...",
            "name": "blue",
            "timestamp": [
              "2018-03-24",
              "15:49:24"
            ]
          },
          {
            "id": "2c951676-...",
            "name": "geen",
            "timestamp": [
              "2018-03-24",
              "15:49:24"
            ]
          }]
    """

    query = Colors.query.all()

    return jsonify([i.serialize for i in query])


@views_bp.route('/', methods=['POST'])
def create_view():
    """Example endpoint return create a color
    ---
    tags:
      - colors
    operationId: get_colors
    consumes:
      - multipart/form-data
    produces:
      - application/json
    schemes: ['http']
    deprecated: false
    parameters:
      - name: name
        in: formData
        type: string
        required: true
        description: Color name
    definitions:
      Color:
        type: object
        properties:
          id:
            type: string
          timestamp:
            type: datetime
          name:
            type: string
    responses:
      200:
        description: The color created
        schema:
          $ref: '#/definitions/Color'
        examples:
          {
            "id": "2c951676-7e6b-4720-971d-9c62e461c74d",
            "name": "blue",
            "timestamp": [
              "2018-03-24",
              "15:49:24"
            ]
          }
    """
    color = Colors(name=request.form["name"])
    db.session.add(color)
    db.session.commit()

    return jsonify(color.serialize)
