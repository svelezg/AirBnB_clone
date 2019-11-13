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
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from unittest.mock import patch
from console import HBNBCommand
import os
from models import storage
import inspect
import console
from unittest import mock
from models import *


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
        """Test the all command"""
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
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
        output3 = f.getvalue().strip()
        # print("newly created object showed by all: {}".format(output3))
        self.assertIn(output2, output3)
        self.assertIn("'created_at': datetime.datetime(", output3)
        self.assertIn("'updated_at': datetime.datetime(", output3)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Not Class")
        output3 = f.getvalue().strip()
        self.assertIn("** class doesn't exist **", output3)

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
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Not a Class')
        output2 = f.getvalue().strip()
        self.assertEqual("** class doesn't exist **", output2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show City " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[City] (" + output1 + ")"), output2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show State " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[State] (" + output1 + ")"), output2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show Place " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[Place] (" + output1 + ")"), output2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show Amenity " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[Amenity] (" + output1 + ")"), output2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show Review " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[Review] (" + output1 + ")"), output2)

    def test_show2(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("User.show(" + output1 + ")")
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[User] (" + output1 + ")"), output2)
        self.assertIn("'created_at': datetime.datetime(", output2)
        self.assertIn("'updated_at': datetime.datetime(", output2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Not a Class')
        output2 = f.getvalue().strip()
        self.assertEqual("** class doesn't exist **", output2)

    def test_count(self):
        """Test the count command"""
        storage.__objects = {}
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.count()')
        output2 = f.getvalue().strip()
        self.assertEqual('1', output2)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        output2 = f.getvalue().strip()
        self.assertEqual('2', output2)

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

    def test_destroy2(self):
        """Test the destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("User.destroy(" + output1 + ")")
            HBNBCommand().onecmd(my_input)
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show User " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn("** no instance found **", output2)

    def test_destroy_errors(self):
        """Test the destroy command error messages"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("destroy")
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertEqual("** class name missing **", output2)
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("destroy User")
            HBNBCommand().onecmd(my_input)
        output3 = f.getvalue().strip()
        self.assertIn("** instance id missing **", output3)
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("destroy User 89698")
            HBNBCommand().onecmd(my_input)
        output4 = f.getvalue().strip()
        self.assertIn("** no instance found **", output4)

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

    def test_update2(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input1 = str("User.update(" + output1 + ', "name",'
                                                       '"test this name")')
            HBNBCommand().onecmd(my_input1)
        with patch('sys.stdout', new=StringIO()) as f:
            my_input2 = str("show User " + output1)
            HBNBCommand().onecmd(my_input2)
        output2 = f.getvalue().strip()
        self.assertIn(str("[User] (" + output1 + ")"), output2)
        self.assertIn("'created_at': datetime.datetime(", output2)
        self.assertIn("'updated_at': datetime.datetime(", output2)

    def test_update_errors(self):
        """Test the destroy command error messages"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("update")
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertEqual("** class name missing **", output2)
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("update User")
            HBNBCommand().onecmd(my_input)
        output3 = f.getvalue().strip()
        self.assertIn("** instance id missing **", output3)
        with patch('sys.stdout', new=StringIO()) as f:
            my_input = str("update User 89698")
            HBNBCommand().onecmd(my_input)
        output4 = f.getvalue().strip()
        self.assertIn("** no instance found **", output4)

    def test_module_documentation(self):
        ''' check module documentation '''
        doc = True
        try:
            len(console.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} module"
        self.assertEqual(
            True, doc, mesg.format(console.__name__))

    def test_class_documentation(self):
        ''' check class HBNBCommand documentation '''
        doc = True
        try:
            len(HBNBCommand.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} class"
        self.assertEqual(
            True, doc, mesg.format(HBNBCommand.__name__))

    def with_mock(self, cmd, expected):

        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            HBNBCommand().onecmd(cmd)
            output = std_out.getvalue()
            self.assertEqual(output.strip(), expected.strip())

    def test_console_help(self):
        expected = ("Documented commands (type help <topic>):\n"
                    "========================================\n"
                    "EOF  all  create  destroy  help  quit  show  update\n")
        self.with_mock(cmd="help", expected=expected)

    def test_exit(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_create_l(self):
        self.with_mock(cmd="create", expected="** class name missing **")
        self.with_mock(cmd="create MyModel",
                       expected="** class doesn't exist **")
        self.with_mock(cmd="create MyModel",
                       expected="** class doesn't exist **")

    def test_show(self):
        self.with_mock(cmd="show", expected="** class name missing **")
        self.with_mock(cmd="show MyModel",
                       expected="** class doesn't exist **")
        self.with_mock(cmd="show BaseModel",
                       expected="** instance id missing **")

    def test_destroy_l(self):
        self.with_mock(cmd="destroy", expected="** class name missing **")
        self.with_mock(cmd="destroy MyModel",
                       expected="** class doesn't exist **")
        self.with_mock(cmd="destroy BaseModel",
                       expected="** instance id missing **")
        self.with_mock(cmd="destroy BaseModel 121212",
                       expected="** no instance found **")

    def test_all_l(self):
        self.with_mock(cmd="all MyModel",
                       expected="** class doesn't exist **")

    def test_update_l(self):
        self.with_mock(cmd="update", expected="** class name missing **")
        self.with_mock(cmd="update MyModel",
                       expected="** class doesn't exist **")
        self.with_mock(cmd="update BaseModel",
                       expected="** instance id missing **")
        self.with_mock(cmd="update BaseModel 121212",
                       expected="** no instance found **")

    def test_show_object(self):

        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = BaseModel()
            HBNBCommand().onecmd("show BaseModel {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = City()
            HBNBCommand().onecmd("show City {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = Place()
            HBNBCommand().onecmd("show Place {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = Review()
            HBNBCommand().onecmd("show Review {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = State()
            HBNBCommand().onecmd("show State {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = User()
            HBNBCommand().onecmd("show User {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))

    def test_update_dict(self):
        """test update by dict"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        my_input1 = str('User.update("' + output1 + '"' +
                        ", {'first_name': " + '"John", "age": 89})')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(my_input1)
            my_input2 = str("show User " + output1)
            HBNBCommand().onecmd(my_input2)
        output2 = f.getvalue().strip()
        self.assertIn(str("[User] (" + output1 + ")"), output2)
        self.assertIn("'first_name': 'John'", output2)
        self.assertIn("'age': '89'", output2)
        self.assertIn("'updated_at': datetime.datetime(", output2)
        self.assertIn("'created_at': datetime.datetime(", output2)
