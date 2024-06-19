# author :   Frederic Baumeister
# date   :   16th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

from datetime import datetime 
from .database import Base
from sqlalchemy import Column, String, DateTime, Numeric, Integer


class Car(Base):
    """ class containing the representation of a Car in the DB
    """
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, autoincrement=True)
    make = Column(String(15), nullable=False, unique=False)
    model = Column(String(15), nullable=False,unique=False)
    year = Column(Numeric(precision=4, scale=0), nullable=False, unique=False)
        # Technically a float but limiting the scale to 0 it behaves like an Integer, 
        # i choose to do it because it allows me the limit the year to a length to 4 digits 
    color = Column(String(15), nullable=False,unique=False)
    price = Column(Numeric(precision=10, scale=2), nullable=False, unique=False)
    created_at = Column(DateTime, default=datetime.now, unique=False)
    
    def __init__(self, model:str, make:str, year:int, color:str, price:float):
        self.model = model
        self.make = make 
        self.year = year
        self.color = color
        self.price = price 

    def update(self, model:str, make:str, year:int, color:str, price:float):
        self.model = model
        self.make = make 
        self.year = year
        self.color = color
        self.price = price 
    
    def as_dict(self): 
        return {
                'ID': self.id, 
                'model': self.model, 
                'year': self.year, 
                'color': self.color, 
                'price': self.price
            }

    def __repr__(self):
        return f'<Car {self.make}{self.model!r}>'
