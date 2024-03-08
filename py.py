import cmd

class MyConsole(cmd.Cmd):
    intro = "Welcome to the HBnB console. Type 'help' to list commands or 'quit' to exit."
    prompt = "(hbnb) "

    def do_help(self, arg):
        """Display help message."""
        print("Available commands:")
        print("  help - Display this help message")
        print("  quit - Exit the console")

    def do_quit(self, arg):
        """Exit the console."""
        print("Exiting the HBnB console. Goodbye!")
        return True

if __name__ == "__main__":
    MyConsole().cmdloop()

