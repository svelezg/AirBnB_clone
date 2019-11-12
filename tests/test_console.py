#!/usr/bin/python3
"""
Unittest for HBNBCommand class
"""

import unittest
import pep8
import contextlib
from io import StringIO
import io
from datetime import datetime
import datetime
from models.base_model import BaseModel
from models.user import User


class FileStorage(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        try:
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files(['./console.py'])
            self.assertEqual(result.total_errors, 0,
                             "Found code style errors (and warnings).")
        except:
            pass
