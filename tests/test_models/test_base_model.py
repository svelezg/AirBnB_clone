#!/usr/bin/python3
"""
Unittest for Base class
"""

import unittest
import pep8
import contextlib
from io import StringIO
import io
from datetime import datetime
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_class(self):
        b0 = BaseModel()
        self.assertTrue(isinstance(b0, BaseModel))

    def test_attributes(self):
        b0 = BaseModel()
        self.assertTrue(hasattr(b0, 'id'))
        self.assertTrue(hasattr(b0, 'created_at'))
        self.assertTrue(hasattr(b0, 'updated_at'))

    def test_types(self):
        b0 = BaseModel()
        self.assertIs(type(b0.id), str)
        self.assertIs(type(b0.created_at), datetime.datetime)
        self.assertIs(type(b0.updated_at), datetime.datetime)

    def test_id_diff(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_BaseModel_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_documentation(self):
        """
        Test to see if documentation is correct and created
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(BaseModel.__str__.__doc__)
        self.assertTrue(BaseModel.save.__doc__)
        self.assertTrue(BaseModel.to_dict.__doc__)

    def test_instantiation(self):
        other_model = BaseModel()
        self.assertTrue(hasattr(other_model, "created_at"))
        self.assertTrue(hasattr(other_model, "updated_at"))

    def test_display(self):
        """__str__: should print: [<class name>] (<self.id>) <self.__dict__>"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(my_model)
        output = temp_stdout.getvalue().strip()
        self.assertIn("[BaseModel]", output)
        self.assertIn("'my_number': 89", output)
        self.assertIn("'name': 'Holberton'", output)
        self.assertIn("'created_at': datetime.datetime", output)
        self.assertIn("'updated_at': datetime.datetime", output)

    def test_save(self):
        """save(self): updates the public instance attribute updated_at"""
        my_model1 = BaseModel()
        var = my_model1.updated_at
        my_model1.save()
        self.assertNotEqual(var, my_model1.updated_at)

    def test_to_dict(self):
        """to_dict(self): returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        my_model2 = BaseModel()
        my_model2.name = "Juan"
        my_model2.my_number = 82
        my_model_json = my_model2.to_dict()
        self.assertTrue(isinstance(my_model_json, dict))
        self.assertEqual(my_model_json['name'], 'Juan')
        self.assertEqual(my_model_json['my_number'], 82)
        """self.__dict__, only instance attributes set will be returned"""
        """a key __class__ must be added to this dictionary with
        the class name of the object"""
        self.assertIsNot(my_model_json['__class__'], None)
        """created_at and updated_at must be converted to string
        object in ISO format"""
        self.assertEqual(type(my_model_json['created_at']), str)
        self.assertEqual(type(my_model_json['updated_at']), str)

    def test_from_dict(self):
        """__init__(self, *args, **kwargs)"""
        my_model3 = BaseModel()
        my_model3.name = "Pedro"
        my_model3.my_number = 80
        my_model_json = my_model3.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertTrue(isinstance(my_new_model, BaseModel))
        self.assertEqual(my_new_model.name, 'Pedro')
        self.assertEqual(my_new_model.my_number, 80)
        """self.__dict__, only instance attributes set will be returned"""
        self.assertFalse(hasattr(my_new_model, "other"))
        """a key __class__ must be added to this dictionary
        with the class name of the object"""
        self.assertIsNot(my_new_model.__class__, None)
        """created_at and updated_at must be converted to string
        object in ISO format"""
        self.assertEqual(type(my_new_model.created_at), datetime.datetime)
        self.assertEqual(type(my_new_model.updated_at), datetime.datetime)
        self.assertFalse(my_model3 is my_new_model)
