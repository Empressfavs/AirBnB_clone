#!/usr/bin/python3
import cmd


"""Simple command processor for HBnB"""


class HBNBCommand(cmd.Cmd):
    """Set the command prompt"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do not execute anything"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
