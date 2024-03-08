#!/usr/bin/python3
import cmd


"""Simple command processor for HBnB"""


class HBNBCommand(cmd.Cmd):
    """Set the command prompt"""
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
