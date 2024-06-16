# author :   Frederic Baumeister
# date   :   15th june 2024 
# Project:   Python Car Management RESTful API Coding Challenge

import json
import requests

api_url = "http://127.0.0.1:8000/GET/cars/"  # Replace with the actual API endpoint URL

data = {
    "key1": "value1",
    "key2": 123,
    "key3": True
}

headers = {'Content-Type': 'application/json'}
response = requests.get(api_url, headers=headers, json=data)

print(response)