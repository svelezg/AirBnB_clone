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
from models.state import State


class TestUser(unittest.TestCase):

    def test_class(self):
        s0 = State()
        self.assertTrue(isinstance(s0, BaseModel))
        self.assertTrue(isinstance(s0, State))

    def test_attributes(self):
        """state_id: string - empty string: it will be the State.id
        name: string - empty string
        """
        u0 = State()
        self.assertTrue(hasattr(u0, 'id'))
        self.assertTrue(hasattr(u0, 'created_at'))
        self.assertTrue(hasattr(u0, 'updated_at'))
        self.assertTrue(hasattr(u0, 'name'))

    def test_types(self):
        u0 = State()
        self.assertIs(type(u0.id), str)
        self.assertIs(type(u0.created_at), datetime.datetime)
        self.assertIs(type(u0.updated_at), datetime.datetime)
        self.assertIs(type(u0.name), str)

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """Testing docstring
        """
        self.assertIsNotNone(State.__doc__)

    def test_print(self):
        my_state = State()
        my_state.name = "Michigan"
        my_state.save()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(my_state)
        output = temp_stdout.getvalue().strip()
        self.assertIn("[State]", output)
        self.assertIn("'name': 'Michigan'", output)
        self.assertIn("'created_at': datetime.datetime", output)
        self.assertIn("'updated_at': datetime.datetime", output)
