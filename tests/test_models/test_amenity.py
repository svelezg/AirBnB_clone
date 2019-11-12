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
from models.amenity import Amenity


class TestUser(unittest.TestCase):

    def test_class(self):
        s0 = Amenity()
        self.assertTrue(isinstance(s0, BaseModel))
        self.assertTrue(isinstance(s0, Amenity))

    def test_attributes(self):
        """Amenity_id: string - empty string: it will be the Amenity.id
        name: string - empty string
        """
        u0 = Amenity()
        self.assertTrue(hasattr(u0, 'id'))
        self.assertTrue(hasattr(u0, 'created_at'))
        self.assertTrue(hasattr(u0, 'updated_at'))
        self.assertTrue(hasattr(u0, 'name'))
        self.assertTrue(hasattr(u0, 'state_id'))

    def test_types(self):
        u0 = Amenity()
        self.assertIs(type(u0.id), str)
        self.assertIs(type(u0.created_at), datetime.datetime)
        self.assertIs(type(u0.updated_at), datetime.datetime)
        self.assertIs(type(u0.name), str)
        self.assertIs(type(u0.state_id), str)

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """Testing docstring
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_print(self):
        my_Amenity = Amenity()
        my_Amenity.name = "Rollercoaster"
        my_Amenity.save()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(my_Amenity)
        output = temp_stdout.getvalue().strip()
        self.assertIn("[Amenity]", output)
        self.assertIn("'name': 'Rollercoaster'", output)
        self.assertIn("'created_at': datetime.datetime", output)
        self.assertIn("'updated_at': datetime.datetime", output)
