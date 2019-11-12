#!/usr/bin/python3
"""
Unittest for User class
"""

import unittest
import pep8
import contextlib
from io import StringIO
import io
from datetime import datetime
import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):

    def test_class(self):
        u0 = City()
        self.assertTrue(isinstance(u0, BaseModel))
        self.assertTrue(isinstance(u0, City))

    def test_attributes(self):
        """email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
        """
        u0 = City()
        self.assertTrue(hasattr(u0, 'id'))
        self.assertTrue(hasattr(u0, 'created_at'))
        self.assertTrue(hasattr(u0, 'updated_at'))
        self.assertTrue(hasattr(u0, 'state_id'))
        self.assertTrue(hasattr(u0, 'name'))

    def test_types(self):
        u0 = City()
        self.assertIs(type(u0.id), str)
        self.assertIs(type(u0.created_at), datetime.datetime)
        self.assertIs(type(u0.updated_at), datetime.datetime)
        self.assertIs(type(u0.state_id), str)
        self.assertIs(type(u0.name), str)

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """Testing docstring
        """
        self.assertIsNotNone(City.__doc__)

    def test_print(self):
        my_city = City()
        my_city.first_name = "Betty"
        my_city.last_name = "Holberton"
        my_city.email = "airbnb@holbertonshool.com"
        my_city.password = "root"
        my_city.save()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(my_city)
        output = temp_stdout.getvalue().strip()
        self.assertIn("[City]", output)
        self.assertIn("'first_name': 'Betty'", output)
        self.assertIn("'last_name': 'Holberton'", output)
        self.assertIn("'created_at': datetime.datetime", output)
        self.assertIn("'updated_at': datetime.datetime", output)
        self.assertIn("'email': 'airbnb@holbertonshool.com'", output)
        self.assertIn("'password': 'root'", output)
