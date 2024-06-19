# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

from .car import Car
from .common import db 

from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

from .database import db_session

class Endpoints:


    @staticmethod
    def get_request():
        if request.is_json:
            json_data = request.get_json()
            offset = json_data['offset'] if json_data['offset'] else 0
            limit = json_data['limit'] if json_data['limit'] else 5
            cars = db_session.query(Car).limit(limit).offset(offset)
            return [car.as_dict() for car in cars]
        return False

    @staticmethod
    def post_request():
        if request.is_json:
            json_data = request.get_json()
            make, model, year, color, price = json_data['make'], json_data['model'], json_data['year'], json_data['color'], json_data['price']
            db_session.add(Car(make=make, model=model, year=year,color=color, price=price))
            db_session.commit()
            return {'Success': 'Success'},200
        return {'error': 'Error creating user'}

    @staticmethod
    def put_request():
        if request.is_json:
            json_data = request.get_json()
            make, model, year, color, price = json_data['make'], json_data['model'], json_data['year'], json_data['color'], json_data['price']
            row = db_session.query(Car).filter(Car.id == json_data['id']).first()
            if row: 
                row.update(make=make, model=model, year=year, color=color, price=price)
                db_session.commit()
                return {'Success': 'Resource updated'},200
            return {"Failure": f"id {json_data['id']} is not in Resource"},404
        return False

    @staticmethod
    def delete_request():
        if request.is_json:
            json_data = request.get_json()
            row = db_session.query(Car).filter(Car.id == json_data['id']).first()
            if row: 
                db_session.delete(row)
                db_session.commit()
                return json_data
            return {"Failure": f"id {json_data['id']} is not in Resource"},404
        return False

