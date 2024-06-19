# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

from PyCaMa.car import Car
from PyCaMa.common import db 
from PyCaMa.database import db_session

if __name__ == "__main__":
    
    sample_data = [
        ('Porsche', '911', 2020, 'red', 75000.00),
        ('VW', 'Golf', 1994, 'black', 20000.00), 
        ('Audi', 'A3', 2023, 'silver', 25000.00), 
        ('Opel', 'Astra', 2004, 'grey', 39000.00)
    ]
    
    for i in range(12):
        for element in sample_data: 
            new_car = Car(make=element[0], model=element[1], year=element[2],color=element[3], price=element[4])
            db_session.add(new_car)
    
    db_session.commit()
    all_cars = db_session.query(Car).all()
    # Validate the Saved Data
    for i, car in enumerate(all_cars):
        print(f"row:{i} \n\tmake: {car.make}\n\tmodel: {car.model}\n\tyear: {car.year}")
    
    db_session.close()