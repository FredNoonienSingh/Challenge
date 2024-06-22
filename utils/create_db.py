# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

from random import choice

from PyCaMa.car import Car
from PyCaMa.common import db 
from PyCaMa.database import db_session
from utils.util import Utils

if __name__ == "__main__":
    for i in range(100):
        print(i)
        new_car = Utils.random_car() 
        db_session.add(new_car)
    db_session.commit()
    all_cars = db_session.query(Car).all()
        # Validate the Saved Data
    for i, car in enumerate(all_cars):
        print(f"row:{i} \n\tmake: {car.make}\n\tmodel: {car.model}\n\tyear: {car.year}")
    db_session.close()