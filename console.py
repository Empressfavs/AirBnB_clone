#!/usr/bin/python3
import cmd
import re

"""Simple command processor for HBnB"""


class HBNBCommand(cmd.Cmd):
    """Set the command prompt"""


    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_help(self, arg):
        """Help command to display help information"""
        super().do_help(arg)

    def emptyline(self):
        """Do not execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
