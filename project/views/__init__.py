# coding=utf-8
from __future__ import unicode_literals, print_function, absolute_import, division

from flask import Blueprint

views_bp = Blueprint('views', __name__, static_url_path='/static')

from project.views import views