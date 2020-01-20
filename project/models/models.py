# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import datetime

from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey

from project.models.init_db import db


class Film(db.Model):
    """Example model"""
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    pub_date = Column(Date, default=datetime.datetime.now)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    cast = db.relationship("Actor", secondary="film_cast")


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    films = db.relationship("Film", secondary="film_cast")


class FilmCast(db.Model):
    __tablename__ = "film_cast"

    film_id = Column(
        Integer, ForeignKey(Film.id, ondelete="CASCADE"), primary_key=True
    )
    actor_id = Column(
        Integer,
        ForeignKey(Actor.id, ondelete="CASCADE"),
        key="id",
        primary_key=True,
    )
    actor = db.relationship(Actor)
    film = db.relationship(Film)
