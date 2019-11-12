# 0x00. AirBnB clone - The console
Description
This team project is part of the first year curriculum of Holberton School. 
The console for the AirBnB clone is mean to be a command interpreter to manage the AirBnB objects.

The learning objective of the project are:
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function

# Authors
Juan Alberto Londoño
Santiago Velez

# Files
* models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
* tests directory will contain all unit tests.
* console.py file is the entry point of our command interpreter.
* models/base_model.py file is the base class of all our models. It contains common elements:
attributes: id, created_at and updated_at
methods: save() and to_json()
* models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.
