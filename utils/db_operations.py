# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

import sqlite3 

# Got moved to its own file to avoid repeating myself, needed in main.py and in my helper class DataBaseInitializer
# Started as two functions, but i wrapped them in a class because this Challenge states that this should follow OOP Principles

class DataBaseOperations:
    """ Helper Class holding methods from database manipulations 

    Methods:
        get_connection
        get_cursor
    """
    
    @staticmethod
    def get_connection(path:str) -> sqlite3.Connection:
            """ establishes a connection to a DB by Path 

            Args:
                path (str): path to the DB 

            Returns:
                sqlite3.Connection: Connection 
            """ 
            conn:sqlite3.Connection = sqlite3.connect(path)
            conn.row_factory = lambda C, R: { c[0]: R[i] for i, c in enumerate(C.description) }
            # in previous projects the in sqlite inbuilt rowfactory caused issues,
            # therefore i started to use this anonymous function instead
            return conn

    @staticmethod
    def get_cursor(connection:sqlite3.Connection) -> sqlite3.Cursor:
            """
                Returns a sqlite3 Cursor for a given Connection 
            Args:
                 connection (sqlite3.Connection): Connection to a DB

            Returns:
                sqlite3.Cursor: Cursor on connected DB 
            """
            return connection.cursor()

    @staticmethod
    def delete_entry() -> bool:
        pass 
    
    @staticmethod
    def update_entry() -> bool: 
        pass 

    @staticmethod
    def create_entry() -> bool: 
        pass 

    @staticmethod
    def fetch_data() -> dict: 
        pass 
