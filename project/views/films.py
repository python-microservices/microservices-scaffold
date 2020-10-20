from datetime import datetime
from typing import Tuple

import connexion
from flask import jsonify
from sqlalchemy.orm import joinedload

from project.models.init_db import db
from project.models.models import Film, FilmCast
from project.serializers.serializers import FilmSchema


def get() -> Tuple[dict, int]:
    query = Film.query.options(
        joinedload(Film.cast),
    ).paginate(
        connexion.request.args.get("paginationKey", 1),
        connexion.request.args.get("pageSize", 5)
    )
    schema = FilmSchema()
    result = schema.dump(query.items, many=True)
    return jsonify(result), 200


def search() -> Tuple[dict, int]:
    return get()


def post() -> dict:
    if connexion.request.is_json:
        data = connexion.request.get_json()
        film = Film(name=data["name"], pub_date=datetime.strptime(data["pubDate"], "%Y-%m-%d").date())
        db.session.add(film)
        db.session.commit()
        film_cast = []
        for actor in data.get("cast", []):
            if actor["id"]:
                film_cast.append(FilmCast(film_id=film.id, actor_id=actor["id"]))
        db.session.add_all(film_cast)
        db.session.commit()

        return jsonify(FilmSchema().dump(film))
    return jsonify({})


def put(id: int) -> dict:
    if connexion.request.is_json:
        data = connexion.request.get_json()
        film = Film.query.filter_by(id=id).first()
        film.name = data["name"]
        film.pub_date = datetime.strptime(data["pubDate"], "%Y-%m-%d").date()
        FilmCast.query.filter_by(film=film).delete()
        film_cast = []
        for actor in data.get("cast", []):
            if actor["id"]:
                film_cast.append(FilmCast(film_id=film.id, actor_id=actor["id"]))
        db.session.add(film)
        db.session.add_all(film_cast)
        db.session.commit()

        return jsonify(FilmSchema().dump(film))
    return jsonify({})
