import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '  # Custom prompt for the command line

    # Dictionary to simulate the database
    objects = {}

    def do_create(self, args):
        """Create command to create a new instance of BaseModel"""
        args = args.split() # Split the arguments
        if not args:
            print("** class name missing **") # Check for missing class name
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **") # Check for existing class name
            return
        obj = BaseModel()  # Create object, assuming BaseModel is defined elsewhere
        obj.save()        # Save object to JSON, assuming save method is implemented
        print(obj.id)     # Print the ID of the object

    def do_show(self, args):
        """Show command to print the string representation of an instance"""
        args = args.split() # Split the arguments
        if len(args) == 0:
            print("** class name missing **") # Check for missing class name
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **") # Check for existing class name
            return
        if len(args) < 2:
            print("** instance id missing **") # Check for missing ID
            return
        obj_key = args[0] + "." + args[1]
        if obj_key not in self.objects:
            print("** no instance found **") # Check if instance exists
            return
        print(self.objects[obj_key]) # Print the object

    # Implement other commands like 'destroy', 'all', and 'update'
    # ...

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

