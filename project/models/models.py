# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import datetime

from sqlalchemy import Column, Integer, String, DateTime

from project.models.init_db import db


def dump_datetime(value: datetime) -> list:
    """Deserialize datetime object into string form for JSON processing."""
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


class Color(db.Model):
    """Example model"""
    __tablename__ = 'colors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.now)

    @property
    def serialize(self) -> dict:
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'timestamp': dump_datetime(self.timestamp),
            'name': self.name,
        }
