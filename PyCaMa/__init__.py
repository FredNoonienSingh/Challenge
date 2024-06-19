from .app import CarAPI
from flask import request
from .common import db


def create_app():
    app = CarAPI(__name__)
    return app