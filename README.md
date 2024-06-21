# Python Car Management Challenge

A RESTful API for managing car models using Python with an object-oriented approach. The API allows users to create, retrieve, update, and delete car models, as well as search and filter car models based on their properties.

<div align="center">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original-wordmark.svg" width="75" heigth="75" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original-wordmark.svg" width="75" heigth="75" />
</div>
<br>

# Table of contents
- [Python Car Management Challenge](#python-car-management-challenge)
- [Table of contents](#table-of-contents)
  - [Setup](#setup)
    - [Linux and macOS](#linux-and-macos)
    - [Windows](#windows)
  - [The Car Object:](#the-car-object)
  - [Endpoints](#endpoints)
    - [*/cars/*](#cars)
    - [__GET__](#get)
      - [To retrieve a single object](#to-retrieve-a-single-object)
      - [**Example Response**](#example-response)
      - [To retrieve multiple objects](#to-retrieve-multiple-objects)
      - [**Example Response**](#example-response-1)
    - [__POST__](#post)
      - [Add a new element to the database](#add-a-new-element-to-the-database)
      - [**Example Response**](#example-response-2)
    - [__PUT__](#put)
      - [Update an element to the database](#update-an-element-to-the-database)
      - [**Example Response**](#example-response-3)
    - [__DELETE__](#delete)
      - [Delete an element from the database](#delete-an-element-from-the-database)
      - [**Example Response**](#example-response-4)
    - [Other Methods](#other-methods)
      - [**Example Response**](#example-response-5)
  - [Design Decision](#design-decision)
    - [Overall Structure](#overall-structure)
    - [The Endpoints Object](#the-endpoints-object)
    - [The Validator Object](#the-validator-object)

## Setup

### Linux and macOS

```bash
git clone git@github.com:FredNoonienSingh/Challenge.git
pip install -e .
flask run 
```


### Windows

Follow this [Guide](https://wiki.archlinux.org/title/installation_guide) and return after you fished the process, an easier but more costly alternative solution can be found [here](https://www.apple.com/de/macbook-pro/).

## The Car Object:

```py
class Car:
      def __init__(self, model:str, make:str, year:int, color:str, price:float):
          self.model = model
          self.make = make 
          self.year = year
          self.color = color
          self.price = price 
```

## Endpoints  
### */cars/* 

### __GET__
#### To retrieve a single object

```json
 {
    "id":Integer,
}
```

#### **Example Response**
```json
  {'Data': [{'ID': 57, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2029'}], 'Success': 'returned single row'}
```
  
#### To retrieve multiple objects
```json
{
    "offset": Integer,
    "limit": Integer, 
    "filter":{
        "model":String, 
        "make": String, 
        "color": String,
        "year": Integer, 
        "price": Float
    }
}
```
#### **Example Response**
```json
{'Data': 
    [
        {'ID': 498, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2024'}, 
        {'ID': 499, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2024'}, 
        {'ID': 500, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2024'}, 
        {'ID': 501, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2024'}, 
        {'ID': 502, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2024'}, 
        {'ID': 503, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2024'}, 
        {'ID': 504, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2024'}, 
        {'ID': 505, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2024'}, 
        {'ID': 506, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2024'}, 
        {'ID': 507, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2024'}, 
        {'ID': 508, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2024'}, 
        {'ID': 509, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2024'}
    ], 
    'Success': 'returned 12 values from 0'}
```

### __POST__
#### Add a new element to the database

```json
{
    "model": String, 
    "make": String, 
    "year": Integer,
    "color": String, 
    "price": Float
}
```

#### **Example Response**
```json
    {'Success': 'Resource created'}
```

### __PUT__
#### Update an element to the database
```json
{
    "id": Integer,
    "model":String, 
    "make": String, 
    "color": String,
    "year": Integer, 
    "price": Float
}
```

#### **Example Response**
```json
    {'Success': 'Resource updated'}
```

### __DELETE__
#### Delete an element from the database
```json
 {
    "id":Integer,
}
```

#### **Example Response**
```json
    {'Failure': 'id 52 is not in Resource'}
```

### Other Methods

There are only the four basic `HTTP` Verbs implemented, use of any other verb such as `HEAD`, `PATCH` or similar will result in an `501` Error.
#### **Example Response**
```json
{'Failure': 'Method not Implemented'}
```

## Design Decision

One big drawback of being self-taught is that there are some conventions that one is not necessarily aware of,therefore i am sure that i broke conventions in this project more then once. In the case that i would be hired for the position I would familiarize myself better with the relevant conventions.
I commented on a few places within the code why i made certain choices, never the less i want to provide a more detailed explanation for a few of them.

### Overall Structure

Inspiration for the Structure of the App and the Endpoint object was the way modern telephone systems work, calls need to be switched between different endpoints. Assuming that the callers don't not need to be connect to a specific end, just to a resource, like for as example in a call center.

To visualize how that is relevant to our API, we think about our endpoints like `/get/cars/` as Agents and our Endpoint class a an entire Floor of the Call Center. A call would come in through a so called trunk before it moves through a switch to an extension that handles the before specified problem of the Customer.



### The Endpoints Object

> was to lazy to add 20 routs 

### The Validator Object 

> Name sounded cool 
