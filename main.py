# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

import os 
import json
from typing import List
from collections.abc import Callable

from werkzeug import Response
from flask import Flask, request, make_response, jsonify

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class EndpointHandler():
    """ Wrapper around function that gets invoked by the Endpoint
    """
    def __init__(self, action:Callable) -> None:
        self.action = action 

    def __call__(self, *args, **kwargs) -> Response:
        """ calls the function 

        Returns:
            Response: return value of invoked function wrapped in JSON response with HTTP Status Code 
        """
        response = self.action(*args, **request.view_args)
        return make_response(response)

class CarAPI(Flask): 

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
        self.app.run(**kwargs)

def get_cars() -> dict:
    if request.is_json:
        json_data = request.get_json()
        return json_data
    return False

flask_app = Flask(__name__)
app = CarAPI(flask_app)

app.add_endpoint('/GET/cars/', 'get_cars', get_cars, methods=['GET'])


if __name__ == "__main__":
    app.run(debug=True, port=8000)   
    # Using default (Port: 5000) causes issues on OSX