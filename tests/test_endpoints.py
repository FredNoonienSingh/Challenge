# author :   Frederic Baumeister
# date   :   15th june 2024
# Project:   Python Car Management RESTful API Coding Challenge

import unittest
from PyCaMa.app import Endpoint


class TestEndpoints(unittest.TestCase):
    """ Tests for methods of the Endpoints object 

    Args:
        TestCase: parent class for testcases in the unittest lib
    """
    def test_get_request(self):
        """ tests the get endpoint
        """
        test_data: list = [
            ({"filter": {"key1": {"gt": 2000}}}, 422),
            ({'id': 1},200)
        ]
        for element in test_data:
            self.assertEqual(Endpoint.get_request(element[0])[1],element[1])

    def test_post_request(self):
        """ tests the get endpoint
        """
        test_data: list = [
            ({"filter": {"key1": {"gt": 2000}}}, 422),
            ( {"model": "R8","make": "Audi", "year": 2024,"color": "red","price": 10000.23},201)
        ]
        for element in test_data:
            self.assertEqual(Endpoint.post_request(element[0])[1],element[1])

    def test_put_request(self):
        """test the put endpoint
        """
        test_data: list = [
            ({"filter": {"key1": {"gt": 2000}}}, 422),
            ({"model": "R8","make": "Audi","year": 2024,"color": "red","price": 10000.23},201)
            ]
        for element in test_data:
            self.assertEqual(Endpoint.post_request(element[0])[1],element[1])

    def test_delete_request(self):
        """tests delete request 
        """
        # Will not test a positive example
        test_data: list = [
            ({"filter": {"key1": {"gt": 2000}}}, 422)
            ]
        for element in test_data:
            self.assertEqual(Endpoint.post_request(element[0])[1],element[1])


if __name__ == '__main__':
    unittest.main()
