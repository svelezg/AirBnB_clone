#!/usr/bin/python3
"""
This is the "base" module.
It supplies one class, base.
"""

import models
import json
import uuid
from datetime import datetime
import sys


class BaseModel:
    """
    Base class
    """
    def __init__(self, *args, **kwargs):
        """
        constructor class
        :param id:
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """
        print
        :return:
        """
        return str("[{}] ({}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        :param self:
        :return:
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance:
        :param self:
        :return: my_dict
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict['created_at'].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
