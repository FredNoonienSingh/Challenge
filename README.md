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
      - [Possible responses](#possible-responses)
      - [**Example Response**](#example-response-1)
    - [__POST__](#post)
      - [Add a new element to the database](#add-a-new-element-to-the-database)
      - [**Example Response**](#example-response-2)
      - [Possible responses](#possible-responses-1)
    - [__PUT__](#put)
      - [Update an element to the database](#update-an-element-to-the-database)
      - [**Example Response**](#example-response-3)
      - [Possible responses](#possible-responses-2)
    - [__DELETE__](#delete)
      - [Delete an element from the database](#delete-an-element-from-the-database)
      - [**Example Response**](#example-response-4)
      - [Possible responses](#possible-responses-3)
    - [Other Methods](#other-methods)
      - [**Example Response**](#example-response-5)
      - [Possible responses](#possible-responses-4)
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

To verify everything is running correctly
```py
python -m unittest discover -v
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
    {'Data': 
    [ 
      {
        'ID': 29, 
        'color': 'red', 
        'make': 'Porsche', 
        'model': '911', 
        'price': '12322.32', 
        'year': '1999'
        }
      ], 
      'Success': 'returned single row'}
```
  
#### To retrieve multiple objects

```js
{
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
```

#### Possible responses

- 200
- 404
- 422

#### **Example Response**

```js
  {'Data': 
  [
    {'ID': 3, 'color': 'silver', 'make': 'Porsche', 'model': '911', 'price': '2849.00', 'year': '1946'},
    {'ID': 5, 'color': 'blue', 'make': 'VW', 'model': 'Astra', 'price': '2448.00', 'year': '1913'}, 
    {'ID': 8, 'color': 'black', 'make': 'Mercedes', 'model': 'Astra', 'price': '1397.00', 'year': '1904'},
    {'ID': 9, 'color': 'blue', 'make': 'Mercedes', 'model': 'A3', 'price': '1379.00', 'year': '1910'}, 
    {'ID': 10, 'color': 'blue', 'make': 'Porsche', 'model': 'R8', 'price': '2424.00', 'year': '1952'}, 
    {'ID': 11, 'color': 'black', 'make': 'BMW', 'model': 'R8', 'price': '2317.00', 'year': '1952'}, 
    {'ID': 12, 'color': 'silver', 'make': 'BMW', 'model': '911', 'price': '2868.00', 'year': '1919'}, 
    {'ID': 13, 'color': 'white', 'make': 'Audi', 'model': 'R8', 'price': '2907.00', 'year': '1991'}, 
    {'ID': 14, 'color': 'red', 'make': 'BMW', 'model': 'Astra', 'price': '1819.00', 'year': '1961'}, 
    {'ID': 15, 'color': 'blue', 'make': 'VW', 'model': 'A3', 'price': '1380.00', 'year': '1991'}, 
    {'ID': 16, 'color': 'silver', 'make': 'Porsche', 'model': 'Astra', 'price': '2233.00', 'year': '1961'},
    {'ID': 17, 'color': 'silver', 'make': 'Mercedes', 'model': 'Astra', 'price': '1048.00', 'year': '1919'}
  ], 'Success': 'returned 12 values from 0'}
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

#### Possible responses

- 201
- 422

### __PUT__

#### Update an element to the database

```js
 {
    'id': 29,
    'data':{
        "model": String, 
        "make": String, 
        "year": Integer,
        "color": String, 
        "price": Float
        }
    }
```


#### **Example Response**

```js
    {'Success': 'Resource updated'}
```

#### Possible responses

- 200
- 404
- 405
- 422

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

#### Possible responses

- 204
- 404
- 422

### Other Methods

There are only the four basic `HTTP` Verbs implemented, use of any other verb such as `HEAD`, `PATCH` or similar will result in an `501` Error.

#### **Example Response**

```js
{'Failure': 'Method not Implemented'}
```

#### Possible responses

- 501

## Design Decision

One big drawback of being self-taught is that there are some conventions that one is not necessarily aware of, therefore i have to assume that i broke conventions in this project more then once. In the case that i would be hired for the position I would familiarize myself better with the relevant conventions.
I commented on a few places within the code why i made certain choices, never the less i want to provide a more detailed explanation for a few of them.

### Overall Structure

Inspiration for the Structure of the App and the Endpoint object was the way modern telephone systems work, calls need to be switched between different endpoints. Assuming that the callers don't not need to be connect to a specific end, just to a 'function', like for as example in a call center.

To visualize how that is relevant to our API, we think about our endpoints like `/get/cars/` as Agents and our Endpoints class a trunk connecting calls. A call would come in through the trunk before it moves through a switch to an extension that handles the before specified problem of the Customer. If we now think about resources on the database like departments in our center, it becomes apparent, that it would be wise to layout the center in a way that each department is served by its own trunk and switch.
Similarly to this Idea is the App layed out, each resource gets its own Endpoints object containing a switch.
Because there is only on resource handled in the App, i decided against building a parent class and wrote an implementation that is specific to the resource at hand. If the need to handle multiple resources would arise, it would be possible to abstract the Endpoint class further so that it can be used as a parent class for resource specific Endpoints Objects to inherit from.

### The Endpoints Object

To Implement the Trunk/switch idea i wrote a \_\_call\_\_ () method containing a switch case, which also allowed me to return a `501`Error if needed.The switch case moves requests to a `staticmethod` that handles the request, after the request got validated by the [Validator](#the-validator-object)

### The Validator Object

The Validator moves trough the requirements of the method that is validating and returns `False` when a requirement is not met or `True` if none of the checks failed.
