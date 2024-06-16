# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

import sqlite3
from db_operations import DataBaseOperations

class DataBaseInitializer:
    def __init__(self, 
                 DB_PATH: str, 
                 DB_USER:str=None, 
                 DB_PASS:str=None
                 ) -> None:
        self.__path = DB_PATH
        self.__user = DB_USER   # in this case not used 
        self.__pass = DB_PASS   # in this case not used 

    # Because this is for an job application:
    #    I am using an double underscore in front of the Name to get something approximating a private variable,
    #    even tho there are no real private variables in Python the dunder in front of the name causes the interpreter to
    #    mangle the name so it can be accessed from outside the class, which is desirable behavior in this case
