#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")  # To print a newline before exiting
        return True

    def do_help(self, arg):
        """Help command to display help information"""
        super().do_help(arg)

    def emptyline(self):
        """Do nothing on an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
