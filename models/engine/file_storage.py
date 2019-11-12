#!/usr/bin/python3
"""
This is the "file storage" module.
It supplies one class, FileStorage.
"""

import copy
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

import uuid
from datetime import datetime
import sys


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        :return:
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        :param obj:
        :return:
        """
        self.__objects[str(type(obj).__name__ + "." + obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        :return:
        """
        my_dict = copy.deepcopy(self.__objects)
        for key, value in my_dict.items():
            my_dict[key] = my_dict[key].to_dict()
        my_json = json.dumps(my_dict)
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(my_json)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        :return:
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                dict_input = f.read()
                dict_output = json.loads(dict_input)

                for k, value in dict_output.items():
                    self.__objects[k] = globals()[value['__class__']](**value)

        except Exception:
            pass
