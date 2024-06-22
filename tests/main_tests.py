# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

from unittest import TestCase
from PyCaMa.app import Endpoint
from utils.operator_map import operator_map

class TestEndpoints(TestCase):
    """ Tests for methods of the Endpoints object 

    Args:
        TestCase: parent class for testcases in the unittest lib
    """
    def test_parse_filter():
        # Only method that does not require the app to be running
         
         test_data: list = [
                {"filter":{"key1": {"gt": 2000}}},
                {"filter":{"key2": {"eq": False}}}
            ]
 