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

    def do_EOF(self, arg):
        """Exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
