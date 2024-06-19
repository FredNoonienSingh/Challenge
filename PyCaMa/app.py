# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

from typing import List
from collections.abc import Callable     #imported for typing, typing.Callable is deprecated since 3.9

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .car import Car
from .endpoints import Endpoints
from .endpointhandler import EndpointHandler
from .database import db_session, init_db

class CarAPI(Flask): 
    """ Main Class of the API inhering from Flask, to structure the project in  
    """
    def __init__(self, name:str, **configs) -> None: 
        super().__init__(name)
        self.configs(**configs)
        init_db()
        
        self.add_endpoint('/cars/', 'get_cars', Endpoints.get_request, methods=['GET'])
        self.add_endpoint('/cars/', 'add_car', Endpoints.post_request, methods=['POST'])
        self.add_endpoint('/cars/', 'update_car', Endpoints.put_request, methods=['PUT'])
        self.add_endpoint('/cars/', 'delete_car', Endpoints.delete_request, methods=['DELETE'])

    def configs(self, **configs) -> None:
        for config, value in configs:
            self.name.config[config.upper()] = value

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
            uri (str): URI of the Endpoint in the Format /resource/'
            endpoint_name (str): Name of the Endpoint.
            function (Callable, optional):
            methods (List[str], optional): List of VERBS. Defaults to ['GET'].
        """
        self.add_url_rule(uri, endpoint_name, EndpointHandler(function), methods=methods, *args, **kwargs)


    def teardown_appcontext(self):
        db_session.remove()
        super().teardown_appcontext()

    def run(self, **kwargs) -> None:
        self.run(**kwargs)