# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge


from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Car:
    """ Dataclass representing a Car as specified in the Challenge

    Attributes
    ----------
    make : str
        make of the Car 
    model : str
        model of the Car
    year : int
        year in which the Car was first registered 
    color: str
        color of the Car
    price: float
        price of the Car
    """ 
    def __init__(self, 
                    make: str, 
                    model: str, 
                    year: int, 
                    color: str, 
                    price: float
                  ) -> None:
        self.make = make 
        self.model = model
        self.year = year 
        self.color = color 
        self.price = price
        # The ID will be given to the object as the primary key in the database when adding the object

