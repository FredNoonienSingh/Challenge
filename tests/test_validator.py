# author :   Frederic Baumeister
# date   :   15th june 2024
# Project:   Python Car Management RESTful API Coding Challenge

import unittest
from PyCaMa.endpoints import Validator # to avoid circular imports


class TestValidator(unittest.TestCase):
    """ Tests for methods of the Validator object 

    Args:
        TestCase: parent class for testcases in the unittest lib
    """
    def test_validate_car(self):
        """ Tests the validate_car method in the Validator Class
        """
        test_data:list = [
            {'PS': 130, 'Seats': 5, 'doors': 4}, 
             {"model": "R8","make": "Audi","year": 2024,"color": 23,"price": 10000.23}
        ]
        for element in test_data:
            self.assertFalse(Validator.validate_car(element))

    def test_validate_get_request(self):
        """ Tests the validate_get_request method in the Validator Class 
        """
        test_data: dict = {'id': 1}
        self.assertTrue(Validator.validate_get_request(test_data))

    def test_validate_get_params(self):
        """ Tests the validate_get_params method in the Validator Class
        """
        test_data:dict = { "offset": None,
            "limit": 12,
            "filters": {
                "year": {
                    "operator": 'lt',
                    "value": 2000
                }
            },
            "model": {
                "operator": 'eq',
                "value": '911'
            }
        }
        self.assertTrue(Validator.validate_get_params(test_data))

if __name__ == '__main__':
    unittest.main()
