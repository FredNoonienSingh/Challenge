# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

from .car import Car
from datetime import datetime 

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, String, DateTime, Numeric, Integer


Base = declarative_base()

if __name__ == "__main__":
    DB_PATH = "database.db"
 
    engine = create_engine(f'sqlite:///{DB_PATH}')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    sample_data = [
        ('Porsche', '911', 2020, 'red', 75000.00),
        ('VW', 'Golf', 1994, 'black', 20000.00), 
        ('Audi', 'A3', 2023, 'silver', 25000.00), 
        ('Opel', 'Astra', 2004, 'grey', 39000.00)
    ]
    
    for element in sample_data: 
        new_car = Car(make=element[0], model=element[1], year=element[2],color=element[3], price=element[4])
        session.add(new_car)
    
    session.commit()
    all_cars = session.query(Car).all()
    # Validate the Saved Data
    for i, car in enumerate(all_cars):
        print(f"row:{i} \n\tmake: {car.make}\n\tmodel: {car.model}\n\tyear: {car.year}")
    
    session.close()