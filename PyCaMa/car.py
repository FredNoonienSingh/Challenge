# author :   Frederic Baumeister
# date   :   16th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

from datetime import datetime 
from sqlalchemy import Column, String, DateTime, Numeric, Integer

from .database import Base

class Car(Base):
    """ class containing the representation of a Car in the DB
    """
    __tablename__ = 'cars'
    id:int = Column(Integer, primary_key=True, autoincrement=True)
    make:str = Column(String(15), nullable=False, unique=False)
    model:str = Column(String(15), nullable=False,unique=False)
    year:int = Column(Numeric(precision=4, scale=0), nullable=False, unique=False)
        # Technically a float but limiting the scale to 0 it behaves like an Integer, 
        # i choose to do it because it allows me the limit the year to a length to 4 digits 
    color:str = Column(String(15), nullable=False,unique=False)
    price:float = Column(Numeric(precision=10, scale=2), nullable=False, unique=False)
    created_at:datetime = Column(DateTime, default=datetime.now, unique=False)
    
    def __init__(self, model:str, make:str, year:int, color:str, price:float) -> None:
        """ Initializes a Car object

        Args:
            model (str): Model of the Car
            make (str): Make of the Car
            year (int): year in which the car was build
            color (str): color of the car
            price (float): price of the car
        """
        self.model = model
        self.make = make 
        self.year = year
        self.color = color
        self.price = price

    def update(self, model:str, make:str, year:int, color:str, price:float) -> None:
        """ Overwrites Fields of the object with parsed values

        Args:
            model (str): Model of the Car
            make (str): Make of the Car
            year (int): year in which the car was build
            color (str): color of the car
            price (float): price of the car
        """
        self.model = model
        self.make = make
        self.year = year
        self.color = color
        self.price = price 
    
    def as_dict(self) -> dict: 
        return {
                'ID': self.id, 
                'model': self.model,
                'make': self.make,
                'year': self.year, 
                'color': self.color, 
                'price': self.price
            }

    def __repr__(self) -> str:
        return f'<Car {self.make}{self.model!r}>'