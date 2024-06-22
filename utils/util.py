# author :   Frederic Baumeister
# date   :   15th june 2024
# Project:   Python Car Management RESTful API Coding Challenge

from random import choice
from PyCaMa.car import Car

class Utils:
    """ Class holding utility scripts 
    """

    @staticmethod
    def random_car() -> Car:
        """ returns random car Objects
        """
        # the combinations are purely random therefore the most of them will not make much sense
        make: list = ['Porsche', 'Audi', 'VW', 'Opel', 'Mercedes', 'BMW']
        model: list = ['911', 'Astra', 'Golf', 'A3', '3i', 'R8']
        year: list = [x for x in range(1889, 2023, 3)]
        color: list = ['red', 'blue', 'silver', 'black', 'silver', 'white']
        price: list = [x/10 for x in range(10000, 30000, 10)]
        return Car(make=choice(make), model=choice(model), year=choice(year), color=choice(color), price=choice(price))
