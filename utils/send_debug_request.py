# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

import requests
import time

api_url = "http://127.0.0.1:8080/cars/"  # Replace with the actual API endpoint URL

get_data = {
    "id": None,
    "offset": None,
    "limit": None
}

post_data = {
    "model": "R8", 
    "make": "Audi", 
    "year": 2029,
    "color": "red", 
    "price": 10000.23
}

del_data = {
    'id':56,
}

update_data = {
    'id': 129,
    'model':"updated", 
    'make': "updated", 
    'color': "updated",
    'year': 1999, 
    'price': 1232232
}

headers = {'Content-Type': 'application/json'}
methods = (
    (requests.get, get_data), 
    (requests.post, post_data), 
    (requests.delete, del_data), 
    (requests.put, update_data)
           )
def test():
    for meth in methods:
        time.sleep(0.2)
        response = meth[0](api_url, headers=headers, json=meth[1])
        try: 
            print(response.json())
        except Exception as e: 
            print(e)

for i in range(25):
    print(f"test run {i+1}")
    test()