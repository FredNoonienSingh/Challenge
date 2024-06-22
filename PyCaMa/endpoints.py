# author :   Frederic Baumeister
# date   :   15th june 2024
# Project:   Python Car Management RESTful API Coding Challenge

from flask import request   # imported for typing

from .car import Car
from .database import db_session
from utils.validator import Validator
from utils.operator_map import operator_map


class Endpoint:
    """
        Object that holds methods for all types of requests 
    """

    def __call__(self) -> dict:
        """ makes the object itself callable 

        Returns:
            dict: response to Endpointhandler 
        """
        # Used this implementation to catch not implemented methods and return an 501 Error
        if request.is_json:
            json_data: dict = request.get_json()
            match request.method:
                case 'GET':
                    return self.get_request(json_data)
                case 'POST':
                    return self.post_request(json_data)
                case 'PUT':
                    return self.put_request(json_data)
                case 'DELETE':
                    return self.delete_request(json_data)
                case _:
                    return {'Failure': 'Method not Implemented'}, 501
        return {'Failure': 'Request not valid'}, 400

    @staticmethod
    def parse_filter(filter_data: dict, field: str):
        """ translates the filter in request to a executable function 

        Args:
            filter_data (dict): dict containing 
            field (str): field to be filters 

        Returns:
            _type_: executable filter 
        """
        operator_dict: dict = dict(filter_data.items())
        operator: str = operator_dict.get('operator')
        value: any = operator_dict.get('value')
        return operator_map.get(operator)(getattr(Car, field), value)

    @staticmethod
    def get_request(data: dict) -> dict:
        """handles get requests 

        Args:
            data (dict): payload of validated request
        """
        # inner functions are used to make the logic when which is used more readable and
        #  to avoid parsing the request body to other functions
        def single_row() -> dict:
            Id: int = data['id']
            row: dict = db_session.query(Car).filter(Car.id == Id).first()
            if row:
                return {'Success': 'returned single row', 'Data': [row.as_dict()]}, 200
            return {"Failure": f"id {data['id']} is not in Resource"}, 404

        def multiple_rows() -> dict:
            offset: int = data['offset'] if data['offset'] else 0
            limit: int = data['limit'] if data['limit'] else 20
            criteria: dict = data.get('filters', {})

            query = db_session.query(Car)

            for field, filter_data in criteria.items():
                filter_func = Endpoint.parse_filter(filter_data, field)
                query = query.filter(filter_func)

            cars: dict = query.offset(offset).limit(limit)
            return {'Success': f'returned {limit} values from {offset}', 'Data': [car.as_dict() for car in cars]}, 206

        if not Validator.validate_get_request(data):
            return {'Failure': 'Request not valid'}, 422
        if 'id' in list(data.keys()):
            return single_row()
        return multiple_rows()

    @staticmethod
    def post_request(data: dict) -> dict:
        """ handles a post request 

        Args:
            data (dict): request body 

        Returns:
            dict: response 
        """
        if not Validator.validate_car(data):
            return {'Failure': 'Request not valid'}, 422
        make, model, year, color, price = data['make'], data['model'], data['year'], data['color'], data['price']
        db_session.add(Car(make=make, model=model, year=year, color=color, price=price))
        db_session.commit()
        return {'Success': 'Resource created'}, 201

    @staticmethod
    def put_request(data: dict) -> dict:
        """ handles a put request 

        Args:
            data (dict): request body 

        Returns:
            dict: response 
        """
        if not Validator.validate_car(data):
            return {'Failure': 'Request not valid'}, 422
        make, model, year, color, price = data['make'], data['model'], data['year'], data['color'], data['price']
        row: dict = db_session.query(Car).filter(Car.id == data['id']).first()
        if row:
            row.update(make=make, model=model, year=year, color=color, price=price)
            db_session.commit()
            return {'Success': 'Resource updated'}, 200
        return {"Failure": f"id {data['id']} is not in Resource"}, 404

    @staticmethod
    def delete_request(data: dict) -> dict:
        """ handles a delete request 

        Args:
            data (dict): request body 

        Returns:
            dict: response 
        """
        Id: int = data['id']
        if not Validator.validate_id(Id):
            return {'Failure': 'Request not valid'}, 422
        row: dict = db_session.query(Car).filter(Car.id == data['id']).first()
        if row:
            db_session.delete(row)
            db_session.commit()
            return {'Success': 'Success'}, 204
        return {"Failure": f"id {data['id']} is not in Resource"}, 404
