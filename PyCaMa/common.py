# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()

SWAGGER_URL = '/api/docs'  
API_URL = 'http://petstore.swagger.io/v2/swagger.json' 


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={ 
        'app_name': "PyCaMa"
    },
)