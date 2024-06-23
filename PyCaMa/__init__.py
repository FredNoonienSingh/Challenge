# author :   Frederic Baumeister
# date   :   15th june 2024
# Project:   Python Car Management RESTful API Coding Challenge

""" 
    A RESTful API for managing car models using Python with an object-oriented approach. 
    The API allows users to create, retrieve, update, and delete car models, 
    as well as search and filter car models based on their properties.
"""
from .app import CarAPI

def create_app() -> CarAPI:
    """creates app 

    Returns:
        CarAPI: child class of Flask.App 
    """
    app: CarAPI = CarAPI(__name__)
    return app
