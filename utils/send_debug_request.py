# author :   Frederic Baumeister
# date   :   15th june 2024
# Project:   Python Car Management RESTful API Coding Challenge

# Script used for debugging the Validator and Endpoint objects

import time
import requests

api_url: dict = "http://127.0.0.1:8080/cars/"  
# Replace with the actual API endpoint URL

get_single: dict = {
    'id': 29
}

get_data: dict = {
    "offset": None,
    "limit": 12,
    "filters": {
        "year": {
            "operator": 'lt',
            "value": 2000
        }
    },
    "model": {
        "operator": 'eq',
        "value": '911'
    }
}

post_data: dict = {
    "model": "R8",
    "make": "Audi",
    "year": 2024,
    "color": "red",
    "price": 10000.23
}

del_data: dict = {
    'id': 5,
}

update_data: dict = {
    'id': 29,
        'data':{
            'model': "updated",
            'make': "911",
        }
    }

headers: dict = {'Content-Type': 'application/json'}
methods: dict = (
    (requests.get, get_single),
    (requests.get, get_data),
    (requests.post, post_data),
    (requests.put, update_data),
    (requests.delete, del_data),
    (requests.patch, update_data)
)

def test():
    """ sends debug requests 
    """
    
    for meth in methods:
        time.sleep(0.2)
        try:
            response = meth[0](api_url, headers=headers, json=meth[1], timeout=10)
            print(response.json())
            print("\n\n")
        except requests.exceptions.RequestException as e:
            print(e)

if __name__ == "__main__":
    test()
