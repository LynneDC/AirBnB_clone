#!/usr/bin/python3
""" importing cmd module to handle commands """
import cmd


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class represents cmd interpreter for the HBNB program.
    It provides a command line interface for interacting with the program.

    Attributes:
        prompt (str): The prompt string displayed to the user.

    Methods:
        do_quit(arg): Exit the program.
        do_EOF(arg): Exit the program.
        emptyline(): Do nothing on empty line.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Exit the program.

        Args:
            arg: The argument provided with the command.

        Returns:
            True: To exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program.

        Args:
            arg: The argument provided with the command.

        Returns:
            True: To exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty line.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
