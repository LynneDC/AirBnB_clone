#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage



class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    instances = {}
    
    def parse_class_command(self, line):
        parts = line.split(".")
        if len(parts) != 2 or not parts[1].endswith("()"):
            return None
        class_name = parts[0]
        command_name = parts[1][:-2]  # Remove the trailing ()
        if class_name not in globals() or not issubclass(globals()[class_name], BaseModel):
            print("** class doesn't exist **")
            return None
        return class_name, command_name

    def default(self, line):
        """Default method called when input doesn't match any known command.
        It will handle special commands like <class name>.all(), <class name>.count(), and <class name>.show(<id>)."""
        line_parts = line.split('.')
        if len(line_parts) != 2:
            print("*** Unknown syntax: {}".format(line))
            return
        class_name, method_part = line_parts
        method_name, _, params = method_part.partition('(')
        params = params.rstrip(')')

        if method_name == "all":
            self.do_all(class_name)
        elif method_name == "count":
            self.do_count(class_name)
        elif method_name == "show":
            self.do_show(class_name, params.strip('"'))
        else:
            print("*** Unknown syntax: {}".format(line))
            
    def do_count(self, class_name):
        """Usage: <class name>.count()
        Retrieve the number of instances of a given class."""
        if class_name not in globals() or not issubclass(globals()[class_name], BaseModel):
            print("** class doesn't exist **")
            return
        count = sum(isinstance(instance, globals()[class_name]) for instance in self.instances.values())
        print(count)


    def do_create(self, line):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals() or not issubclass(
            globals()[class_name], BaseModel
        ):
            print("** class doesn't exist **")
            return
        obj = globals()[class_name]()
        self.instances[obj.id] = obj
        storage.new(obj)  # Add to FileStorage
        storage.save()  # Save to file.json
        print(obj.id)

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_show(self, line):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals() or not issubclass(
            globals()[class_name], BaseModel
        ):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        if instance_id not in self.instances:
            print("** no instance found **")
            return
        print(self.instances[instance_id])



    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_all(self, line):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args = line.split()
        if args:
            class_name = args[0]
            if class_name not in globals() or not issubclass(
                globals()[class_name], BaseModel
            ):
                print("** class doesn't exist **")
                return
            result = [
                str(instance)
                for instance in self.instances.values()
                if isinstance(instance, globals()[class_name])
            ]
        else:
            result = [str(instance) for instance in self.instances.values()]
        print(result)

    def do_destroy(self, line):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals() or not issubclass(
            globals()[class_name], BaseModel
        ):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        if instance_id not in self.instances:
            print("** no instance found **")
            return
        del self.instances[instance_id]
        key_to_remove = "{}.{}".format(class_name, instance_id)
        # print("Key to remove:", key_to_remove)  # Debug print
        # print("Keys before deletion:", storage.all().keys())  # Debug print
        if key_to_remove in storage.all():  # Check if key exists in FileStorage
            del storage.all()[key_to_remove]  # Remove from FileStorage
        # print("Keys after deletion:", storage.all().keys())  # Debug print
        storage.save()  # Save to file.json

    def do_update(self, line):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
         Update a class instance of a given id by adding or updating
         a given attribute key/value pair or dictionary."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals() or not issubclass(
            globals()[class_name], BaseModel
        ):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        if instance_id not in self.instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')  # Remove quotes
        instance = self.instances[instance_id]
        if attr_name in ["id", "created_at", "updated_at"]:
            return  # Ignore these attributes
        if attr_name in instance.__dict__:
            attr_type = type(instance.__dict__[attr_name])
            attr_value = attr_type(attr_value)  # Cast to correct type
        setattr(instance, attr_name, attr_value)


# Code to run the CLI
if __name__ == "__main__":
    HBNBCommand().cmdloop()

