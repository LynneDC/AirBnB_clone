#!/usr/bin/python3

import cmd
import doctest
import json
import os.path
from  models.base_model import BaseModel
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_create(self, arg):
        if not arg:
            print(" ** class name missing ** ")
            return
        try:
            instance = eval(arg)()
            instace.save()
            print(instance.id)
        except NameError:
            print(" ** class doesn't exist ** ")

    def do_show(self, arg):
        args = arg.split()
        if not args:
            print(" ** class name missing ** ")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            instance = BaseModel.get(class_name, instance_id)
            print(instance)
        except IndexError:
            if len(args) == 1:
                print(" ** instance id missing ** ")
            else:
                print(" ** no instance found ** ")
        except NameError:
            print(" ** class doesn't exist ** ")

    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            instance_id = args[1]
            instance = BaseModel.get(class_name, instance_id)
            if instance:
                instance.delete()
            else:
                print("** no instance found **")
        except IndexError:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):

        if not arg:
            print([str(instance) for instance in BaseModel.all()])
        else:
            try:
                class_name = arg
                print([str(instance) for instance in BaseModel.all(class_name)])
            except NameError:
                print(" ** class doesn't exist ** ")
    def do_update(self, arg):
        args = arg.spit()
        if not args:
            print(" ** class name missing ** ")
            return
        try:
            class_name = args[o]
            instance_id = args[1]
            instance = BaseModel.get(class_name, instance_id)
            if len(args) == 2:
                print(" ** attribute name missing ** ")
            elif len(args) == 3:
                print(" ** value missing ** ")
            else:
                attribute_name = args[2]
                attribute_value = args[3]
                if hasattr(instance, attribute_name):
                    setattr(instance, attribute_name, type(getattr(instance, attribute_name)) (attribute_value))
                    instance.save()
                else:
                    print(" ** attribute doesn't exist **")
        except IndexError:
            if len(args) == 1:
                print(" ** instance id missing **")
            else:
                print(" ** no instance found ** ")
        except NameError:
            print(" ** class doesn't exist ** ")
    @classmethod
    def all(cls):
        return [str(instance) for instance in cls.__objects.values()]

#  def all(self):
#return [str(instance) for instance in self.__objects.values()]

    def do_quit(self, arg):
        """Exit the program"""
        print("Exiting the program...")
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def doctest_help(self, arg):
        """Run doctests for the help command

        Arguments:
        - arg: The argument passed to the help command


        """


if __name__ == "__main__":
    HBNBCommand().cmdloop()

