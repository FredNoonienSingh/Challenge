# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

import requests
import time

api_url:dict = "http://127.0.0.1:8080/cars/"  # Replace with the actual API endpoint URL

get_single:dict = {
    'id': 1
}

get_data:dict = {
    "offset": None,
    "limit": 12, 
    "filter":{
        "year": {
            "operator": "gt", 
            "value": 2000
            }
        }
    }

post_data:dict = {
    "model": "R8", 
    "make": "Audi", 
    "year": 2024,
    "color": "red", 
    "price": 10000.23
}

del_data:dict = {
    'id':52,
}

update_data:dict = {
    'id': 129,
    'model':"updated", 
    'make': "updated", 
    'color': "updated",
    'year': 1999, 
    'price': 12322.32
}

headers:dict = {'Content-Type': 'application/json'}
methods:dict = (
    (requests.get, get_single), 
    (requests.get, get_data), 
    #(requests.post, post_data), 
    #(requests.put, update_data),
    #(requests.delete, del_data), 
    #(requests.patch, update_data)
           )

def test():
    for meth in methods:
        time.sleep(0.2)
        response = meth[0](api_url, headers=headers, json=meth[1])
        try: 
            print(response.json())
        except Exception as e: 
            print(e)

i = 0
while True:
    print(f"test run {i+1}")
    i+=1
    test()