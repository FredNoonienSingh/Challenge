# Python Car Management Challenge

[![Pylint](https://github.com/FredNoonienSingh/Challenge/actions/workflows/pylint.yml/badge.svg)](https://github.com/FredNoonienSingh/Challenge/actions/workflows/pylint.yml)

A RESTful API for managing car models using Python with an object-oriented approach. The API allows users to create, retrieve, update, and delete car models, as well as search and filter car models based on their properties.

<div align="center">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" alt="python" width="200" height="200" />

<br>

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original-wordmark.svg" width="200" heigth="200" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original-wordmark.svg" width="200" heigth="200" />
</div>

<br>

## Table of contents

- [Python Car Management Challenge](#python-car-management-challenge)
  - [Table of contents](#table-of-contents)
  - [Setup](#setup)
    - [Linux and macOS](#linux-and-macos)
    - [Windows](#windows)
  - [The Car Object](#the-car-object)
    - [\_\_ init \_\_()](#__-init-__)
    - [update()](#update)
    - [as\_dict()](#as_dict)
    - [\_\_ repr \_\_()](#__-repr-__)
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

For installing the App it is necessary to have Python 3 installed on your System.
In the first Step clone the repository onto your machine by running:

```bash
git clone git@github.com:FredNoonienSingh/Challenge.git
```

There is no environment file included in the repository, therefore it has to be created

```bash
cd Challenge
vim .flaskenv
```

then paste the following into the file

```py
FLASK_APP='PyCaMa'

FLASK_DEBUG=True 
FLASK_RUN_PORT=8080

SQLALCHEMY_COMMIT_ON_TEARDOWN=True
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
```
More information about the flask env file can be found [here](https://flask.palletsprojects.com/en/2.3.x/config/).

Close the file by pressing `escape` follow by `:wq` Now run the included setup file

```bash
pip install -e .
```

Now create the database file by running:

```bash
touch database.db
```

__OPTIONAL__:

To fill the database with Mock data run

```bash
python3 utils/fill_db.py
```

After this we can start the app by running

```bash
flask run 
```

### Windows

Follow this [Guide](https://wiki.archlinux.org/title/installation_guide) and return after you fished the process, an easier but more costly alternative solution can be found [here](https://www.apple.com/de/macbook-pro/).

## The Car Object

```py
class Car(Base):
      __tablename__ = 'cars'
      id: int = Column(Integer, primary_key=True, autoincrement=True)
      make: str = Column(String(15), nullable=False, unique=False)
      model: str = Column(String(15), nullable=False, unique=False)
      year: int = Column(Numeric(precision=4, scale=0), nullable=False, unique=False)
      color: str = Column(String(15), nullable=False, unique=False)
      price: float = Column(Numeric(precision=10, scale=2), nullable=False, unique=False)
      created_at: datetime = Column(DateTime, default=datetime.now, unique=False)
```

The car object is a representation of a car in the way outlined in the Challenge. It holds the following methods.

### __ init __()

```py
    def __init__(self, model: str, make: str, year: int, color: str, price: float) -> None:
        """ Initializes a Car object

        Args:
            model (str): Model of the Car
            make (str): Make of the Car
            year (int): year in which the car was build
            color (str): color of the car
            price (float): price of the car
        """
        self.model = model
        self.make = make
        self.year = year
        self.color = color
        self.price = price
```

### update()

This method instantiates an object, it does not return a new instance.

```py
    def update(self, data:dict) -> None:
        """ Overwrites Fields of the object with parsed values

        Args:
            data (dict): dictionary containing the field and new data
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
```

Works by checking for each key:value pair in the dict data, if the class has the attribute and if so overwrites the old value of this attribute with the new value.

### as_dict()

```py
    def as_dict(self) -> dict:
        """ returns fields of the object as dict

        Returns:
            dict: fields of the object
        """
        return {
            'ID': self.id,
            'model': self.model,
            'make': self.make,
            'year': self.year,
            'color': self.color,
            'price': self.price
        }
```

Return the a dict with containing the attributes of the class as key with their respective values as value.

### __ repr __()

```py
    def __repr__(self) -> str:
        """ returns string representing the object 

        Returns:
            str: string representing the object
        """
        return f'<Car {self.make}{self.model!r}>'
```

Returns a string representation of the car, it is usually a standard method but I have overwritten it for debugging purposes.

## Endpoints

### */cars/*

### __GET__

#### To retrieve a single object

```js
 {
    "id":Integer,
}
```

#### **Example Response**

```js
  {'Data': [{'ID': 57, 'color': 'red', 'make': 'Audi', 'model': 'R8', 'price': '10000.23', 'year': '2029'}], 'Success': 'returned single row'}
```
  
#### To retrieve multiple objects

```js
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

```js
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

```js
{
    "model": String, 
    "make": String, 
    "year": Integer,
    "color": String, 
    "price": Float
}
```

#### **Example Response**

```js
    {'Success': 'Resource created'}
```

### __PUT__

#### Update an element to the database

```js
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

```js
    {'Success': 'Resource updated'}
```

### __DELETE__

#### Delete an element from the database

```js
 {
    "id":Integer,
}
```

#### **Example Response**

```js
    {'Failure': 'id 52 is not in Resource'}
```

### Other Methods

There are only the four basic `HTTP` Verbs implemented, use of any other verb such as `HEAD`, `PATCH` or similar will result in an `501` Error.

#### **Example Response**

```js
{'Failure': 'Method not Implemented'}
```

## Design Decision

One big drawback of being self-taught is that there are some conventions that one is not necessarily aware of, therefore i have to assume that i broke conventions in this project more then once. In the case that i would be hired for the position I would familiarize myself better with the relevant conventions.
I commented on a few places within the code why i made certain choices, never the less i want to provide a more detailed explanation for a few of them.

### Overall Structure

Inspiration for the Structure of the App and the Endpoint object was the way modern telephone systems work, calls need to be switched between different endpoints. Assuming that the callers don't not need to be connect to a specific end, just to a resource, like for as example in a call center.

To visualize how that is relevant to our API, we think about our endpoints like `/get/cars/` as Agents and our Endpoint class a an entire Floor of the Call Center. A call would come in through a so called trunk before it moves through a switch to an extension that handles the before specified problem of the Customer.

### The Endpoints Object

### The Validator Object
