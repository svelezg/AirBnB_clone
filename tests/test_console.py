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
from unittest.mock import patch
from console import HBNBCommand
import os
from models import storage


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

        def test_not_found(self):
            """Test command interpreter"""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("Non existant")
            output = f.getvalue().strip()
            expected1 = "*** Unknown syntax: Non existant"
            self.assertIn(expected1, output)

    def test_help_show(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        output = f.getvalue().strip()
        expected1 = "Prints the string representation of an instance based"
        expected2 = "        on the class name and id"
        self.assertIn(expected1, output)
        self.assertIn(expected2, output)

    def test_help_quit(self):
        """Test the help quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        output = f.getvalue().strip()
        expected1 = "Quit command to exit the program"
        self.assertIn(expected1, output)

    def test_all(self):
        """Test the help command"""
        storage.__objects = {}
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        output1 = f.getvalue().strip()
        # print("empty{}".format(output1))
        self.assertEqual("", output1)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            HBNBCommand().onecmd("create User")
        output2 = f.getvalue().strip()
        # print("newly created object id: {}".format(output2))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        output3 = f.getvalue().strip()
        # print("newly created object showed by all: {}".format(output3))
        self.assertIn(output2, output3)
        self.assertIn("'created_at': datetime.datetime(", output3)
        self.assertIn("'updated_at': datetime.datetime(", output3)

    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show User " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[User] (" + output1 + ")"), output2)
        self.assertIn("'created_at': datetime.datetime(", output2)
        self.assertIn("'updated_at': datetime.datetime(", output2)

    def test_show_errors(self):
        """Test the show command error messages"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show")
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertEqual("** class name missing **", output2)
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show User")
            HBNBCommand().onecmd(my_input)
        output3 = f.getvalue().strip()
        self.assertIn("** instance id missing **", output3)
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show User 89698")
            HBNBCommand().onecmd(my_input)
        output4 = f.getvalue().strip()
        self.assertIn("** no instance found **", output4)

    def test_destroy(self):
        """Test the destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("destroy User " + output1)
            HBNBCommand().onecmd(my_input)
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show User " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn("** no instance found **", output2)

    def test_update(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input1 = str("update User " + output1 + 'name "test this name"')
            HBNBCommand().onecmd(my_input1)
        with patch('sys.stdout', new=StringIO()) as f:
            my_input2 = str("show User " + output1)
            HBNBCommand().onecmd(my_input2)
        output2 = f.getvalue().strip()
        self.assertIn(str("[User] (" + output1 + ")"), output2)
        self.assertIn("'created_at': datetime.datetime(", output2)
        self.assertIn("'updated_at': datetime.datetime(", output2)
