# author :   Frederic Baumeister
# date   :   16th june 2024
# Project:   Python Car Management RESTful API Coding Challenge

from setuptools import setup, find_packages

with open("README.md", 'r', encoding='UTF-8') as f:
    long_description = f.read()

setup(
    name='PyCaMa',
    version='1.0',
    description='Python Car Management RESTful API Coding Challenge',
    license="MIT",
    long_description=long_description,
    author='Frederic Baumeister',
    author_email='FredBaumeister@Icloud.com',
    url="https://github.com/FredNoonienSingh/Challenge",
    packages=find_packages(),
    install_requires=['Flask', 'Flask-SQLAlchemy', 'pytest', 'python-dotenv'],  # external packages as dependencies
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest'],
    test_suite='tests'
)
