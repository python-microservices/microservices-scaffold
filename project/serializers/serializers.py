from marshmallow_sqlalchemy import ModelSchema

from project.models.models import Color


class ColorSchema(ModelSchema):
    class Meta:
        model = Color
        fields = ('id', 'name', 'timestamp')
