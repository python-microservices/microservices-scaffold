from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from project.models.models import Film, Actor


class ActorSchema(ModelSchema):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'surname')


class FilmSchema(ModelSchema):
    cast = fields.Nested(ActorSchema, many=True)
    pubDate = fields.String(required=True, data_key='pub_date', attribute="pub_date")

    class Meta:
        model = Film
        fields = ('id', 'name', 'pub_date', 'cast')
