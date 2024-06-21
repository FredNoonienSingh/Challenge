# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

from flask import Flask
from typing import List
from collections.abc import Callable     #imported for typing, typing.Callable is deprecated since 3.9

from .database import init_db
from .endpoints import Endpoint
from .endpointhandler import EndpointHandler

class CarAPI(Flask): 
    """ Main Class of the API inhering from Flask, to structure the project in  
    """
    def __init__(self, name:str, **configs) -> None: 
        super().__init__(name)
        self.configs(**configs)
        init_db()

        self.add_endpoint('/cars/', 'cars', Endpoint(), methods=[
            'GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'TRACE', 'OPTIONS','CONNECT','HEAD'
            ])

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
                     ) -> None:
        """ adds an Endpoint to the API 
        Args:
            uri (str): URI of the Endpoint in the Format /resource/'
            endpoint_name (str): Name of the Endpoint.
            function (Callable, optional):
            methods (List[str], optional): List of VERBS. Defaults to ['GET'].
        """
        self.add_url_rule(uri, endpoint_name, EndpointHandler(function), methods=methods, *args, **kwargs)

    def run(self, **kwargs) -> None: 
        self.run(**kwargs)