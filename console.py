#!/usr/bin/python3
"""
This is the "console" module.
It supplies one class, HBNBCommand.
"""

import cmd
import sys
import inspect
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    command line interpreter class
    """
    prompt = '(hbnb) '
    file = None
    list_models = [elem[0] for elem in inspect.getmembers(
        sys.modules[__name__], inspect.isclass)]

    # ["BaseModel", "User", "Place", "State", "City",
    # "Amenity", "Review"]

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Overwrite empty line standard"""

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] in self.list_models:
                my_model = eval(args[0]+"()")
                my_model.save()
                print(my_model.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        if len(arg) != 0:
            args = arg.split()
            if args[0] in self.list_models:
                if len(args) == 2:
                    dict_id = str(args[0] + "." + args[1])
                    my_dict = models.storage.all()
                    if dict_id in my_dict:
                        print(my_dict[dict_id])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        if len(arg) != 0:
            args = arg.split()
            if args[0] in self.list_models:
                if len(args) == 2:
                    dict_id = str(args[0] + "." + args[1])
                    my_dict = models.storage.all()
                    if dict_id in my_dict:
                        del my_dict[dict_id]
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or
        not on the class name
        """
        my_dict = models.storage.all()
        if len(arg) != 0:
            if arg in self.list_models:
                for key in my_dict:
                    if arg in key:
                        print(key)
                        print(my_dict[key])
            else:
                print("** class doesn't exist **")
        else:
            for key in my_dict:
                print(my_dict[key])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        """
        if len(arg) != 0:
            print(arg)
            args_1 = arg.split('"')
            args = args_1[0].split()
            if len(args_1) > 1:
                args.append(args_1[1])
            print(args)
            if args[0] in self.list_models:
                if len(args) >= 2:
                    dict_id = str(args[0] + "." + args[1])
                    my_dict = models.storage.all()
                    if dict_id in my_dict:
                        if len(args) >= 3:
                            if len(args) >= 4:
                                obj = my_dict[dict_id]
                                if args[2] in obj.__dict__:
                                    my_type = type(obj.__dict__[args[2]])
                                    print(eval(args[0]+"."+args[2]))
                                    my_type = type(eval(args[0] + "." +
                                                        args[2]))
                                    obj.__dict__[args[2]] = my_type(args[3])
                                else:
                                    obj.__dict__[args[2]] = args[3]
                                models.storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def default(self, arg):
        args = arg.split(".")
        if args[0] in self.list_models:
            if args[1] == 'all()':
                self.do_all(args[0])
            elif args[1] == 'count()':
                my_dict = models.storage.all()
                count = 0
                for key in my_dict:
                    if args[0] in key:
                        count = count + 1
                print(count)
            elif args[1].split('(')[0] == 'show':
                var = args[1].split('(')[1][:-1]
                aux = str(args[0] + " " + var)
                self.do_show(aux)
            elif args[1].split('(')[0] == 'destroy':
                var = args[1].split('(')[1][:-1]
                aux = str(args[0] + " " + var)
                self.do_destroy(aux)
            elif args[1].split('(')[0] == 'update':
                var = args[1].split('(')[1][:-1]
                values = var.split(',')
                aux = str(args[0] + ' ' + values[0] + values[1] + values[2])
                self.do_update(aux)
        else:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
