#!/usr/bin/python3
"""
Unittest for FileStorage class
"""

import unittest
import pep8
import contextlib
from io import StringIO
import io
import copy
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import os
from os import remove
import contextlib
from io import StringIO

import uuid
from datetime import datetime
import sys


class FileStorage(unittest.TestCase):

    def setUp(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        """save(self): serializes __objects to the JSON
        file (path: __file_path)"""
        my_model.save()

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_class(self):
        f0 = FileStorage()
        self.assertTrue(isinstance(f0, FileStorage))
        # self.assertTrue(hasattr(storage, '__file_path'))
        # self.assertTrue(hasattr(storage, '__objects'))

    def test_types(self):
        try:
            """create the variable storage, an instance of FileStorage"""
            self.assertIs(type(storage.__file_path), str)
            self.assertIs(type(storage.__objects), dict)
            """__file_path: string - path to the JSON file (ex: file.json)"""
            self.assertEqual(storage.__file_path, 'file.json')
        except:
            pass

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        try:
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files(['./models/engine/file_storage.py'])
            self.assertEqual(result.total_errors, 0,
                             "Found code style errors (and warnings).")
        except:
            pass

    def test_storage_all(self):
        """reload(self): deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the
        file doesn’t exist,
        no exception should be raised)"""
        """all(self): returns the dictionary __objects"""
        """call reload() method on storage"""
        all_objs = storage.all()
        self.assertIs(type(all_objs), dict)
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            temp_stdout = StringIO()
            with contextlib.redirect_stdout(temp_stdout):
                print(obj)
            output = temp_stdout.getvalue().strip()
            self.assertIn("'id':", output)
            self.assertIn("'created_at':", output)
            self.assertIn("'updated_at':", output)

    def test_new(self):
        """new(self, obj): sets in __objects the obj with
        key <obj class name>.id"""
        obj = User()
        obj.first_name = "New name"
        obj_id = str("User." + obj.id)
        all_objs = storage.all()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(all_objs[obj_id])
        output = temp_stdout.getvalue().strip()
        self.assertIn("[User]", output)
        self.assertIn("'first_name': 'New name'", output)

    def test_save(self):
        os.remove('file.json')
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        """save(self): serializes __objects to the JSON
        file (path: __file_path)"""
        my_model.save()
        self.assertTrue(os.access('file.json', os.R_OK))
        allobjects = storage.all()
        for obj_id in allobjects.keys():
            if my_model.id in obj_id:
                obj = allobjects[obj_id]
                self.assertEqual(my_model.id, obj.id)
                self.assertEqual(my_model.name, obj.name)
                self.assertEqual(my_model.my_number, obj.my_number)
                self.assertEqual(my_model.created_at, obj.created_at)
                self.assertEqual(my_model.updated_at, obj.updated_at)

    def test_reload(self):
        """deserializes the JSON file to __objects"""
        storage.__objects = {}
        self.assertEqual(len(storage.all()), 0)
        my_model = BaseModel()
        my_model.save()
        storage.__objects = {}
        storage.reload()
        self.assertNotEqual(len(storage.all()), 0)
