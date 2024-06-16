# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

import os 
import json

from typing import List
from collections.abc import Callable     #imported for typing, typing.Callable is deprecated since 3.9

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, make_response

from endpointhandler import EndpointHandler

class CarAPI(Flask): 
    """ Main Class of the API inhering from Flask, to structure the project in  

    Args:
        Flask (_type_): _description_
    """
    def __init__(self, app, **configs) -> None: 
        self.app = app
        self.configs(**configs)

    def configs(self, **configs) -> None:
        for config, value in configs:
            self.app.config[config.upper()] = value

    def add_endpoint(self, 
                        uri:str, 
                        endpoint_name:str, 
                        function:Callable, 
                        methods:List[str]=['GET'], 
                        *args, 
                        **kwargs
                     ):
        """ adds an Endpoint to the API 

        Args:
            uri (str): URI of the Endpoint in the Format 'VERB/resource/<type:payload>'
            endpoint_name (str): Name of the Endpoint.
            function (Callable, optional):
            methods (List[str], optional): List of VERBS. Defaults to ['GET'].
        """
        self.app.add_url_rule(uri, endpoint_name, EndpointHandler(function), methods=methods, *args, **kwargs)

    def run(self, **kwargs) -> None:
        """ Runs the App
        """
        self.app.run(**kwargs)


def get_cars() -> dict:
    if request.is_json:
        json_data = request.get_json()
        return json_data
    return False

def create_car() -> dict: 
    if request.is_json:
        json_data = request.get_json()
        return json_data
    return False

def update_car() -> dict: 
    if request.is_json:
        json_data = request.get_json()
        return json_data
    return False

def delete_car() -> dict: 
    if request.is_json:
        json_data = request.get_json()
        return json_data
    return False

flask_app = Flask(__name__)
app = CarAPI(flask_app)
db = SQLAlchemy()

app.add_endpoint('/GET/cars/', 'get_cars', get_cars, methods=['GET'])
app.add_endpoint('/POST/cars/', 'create_car', create_car, methods=['POST'])
app.add_endpoint('/PUT/cars/', 'update_car', update_car, methods=['PUT'])
app.add_endpoint('/GET/cars/', 'delete_car', delete_car, methods=['DELETE'])

if __name__ == "__main__":
    app.run(debug=True, port=8000)   
    # Using default (Port: 5000) causes issues on OSX