# author :   Frederic Baumeister
# date   :   17th june 2024
# Project:   Python Car Management RESTful API Coding Challenge

from types import NoneType
from datetime import datetime
from numbers import Number
from PyCaMa.car import Car

class Validator:
    """ Class holding static Methods to validate Inputs 
    """
    
    @staticmethod
    def validate_car(data:dict) -> bool:
        """ Validates that all values are 

        Args:
            data (dict): dictionary with keys and values corresponding to a car object 

        Returns:
            bool: False if any of the Values are of the wrong type or are not in Range 
        """
        expected_keys:set = set(['make', 'model', 'year', 'color', 'price'])
        if not expected_keys.issubset(data.keys()):
            return False
        make, model, year, color, price = data['make'],data['model'],data['year'],data['color'],data['price']
        # Validate Strings: 
        if not isinstance(make,str) or not isinstance(model,str) or not isinstance(color,str):
            return False 
        # Validate Price 
        if not isinstance(price,float) or price<0:
            return False
        # Validate Year
        # a car could not be build in a year after then the current year and there were no cars before 1886
        if not isinstance(year, int) or year > int(datetime.now().strftime('%Y')) or year < 1886: 
            return False 
        return True
 
    @staticmethod
    def validate_get_request(data:dict) -> bool:
        """ Validates a get request 

        Args:
            data (dict): body of the Request 

        Returns:
            bool: returns False if the request is not valid 
        """
        keys: list = list(data.keys())
        if 'id' in keys:
             return Validator.validate_id(data['id'])
        return Validator.validate_get_params(data)

    @staticmethod
    def validate_id(Id:int) -> bool:
        """ Validates an ID before it is used to access a row in the DB 

        Args:
            Id (int): id 

        Returns:
            bool: False if id is not an Integer or smaller than 0
        """
        if not Id > 0 or not isinstance(Id, int):
            return False 
        return True 
    
    @staticmethod
    def validate_get_params(data:dict) -> bool:
        """ Validates the parameters of a get request

        Args:
            data (dict): body of the request

        Returns:
            bool: False if wrong params are parsed 
        """
        params:tuple = data['offset'], data['limit']
        for el in params:
            if not isinstance(el, int) and not isinstance(el, NoneType):
                return False 
            if isinstance(el, int) and el < 0:
                return False 
        filter_params:dict = data['filters']
        return Validator.validate_filter_params(filter_params)
    
    @staticmethod
    def validate_filter_params(data:dict) -> bool:
        """ Validates the filter Params of a get request

        Args:
            data (dict): filters: dict from get request Body

        Returns:
            bool: False if params are not valid 
        """
        for field, filter_data in data.items():
            
            if field not in Car.__dict__.keys():
                return False
            
            operator_dict:dict = dict(filter_data.items())
            operator:str = operator_dict.get('operator')
            value:any = operator_dict.get('value')

            if not isinstance(value, Number):
                if operator in ['eq', 'gt', 'lt', 'gte', 'lte']:
                    return False
            
        return True 