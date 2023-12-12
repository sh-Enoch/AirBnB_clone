#!/usr/bin/python3
"""Entry point of the interpreter."""
import cmd
from models.base_model  import BaseModel

class HBNBCommand(cmd.Cmd):
    """Define class HBNBCommand."""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Exit program."""
        return True

    def do_help(self, arg):
        """Show commands to guide user."""
        if arg:
            super().do_help(arg)
        else:
            print()
            print("Documented commands (type help <topic>):")
            print("========================================")
            for cmd in self.get_names():
                if cmd.startswith('do_'):
                    print("{}".format(cmd[3:]), end=" ")
            print()
            print()

    def do_EOF(self):
        """Exit program."""
        print()
        return True

    def emptyline(self):
        """Shouldn't execute anything on new line."""
        pass

    def do_create(self, className):
        """Create a new instance of BaseModel."""
        if className:
            if className != "BaseModel":
                print("class doesn't exist")
            else:
                new_instance = BaseModel()
                new_instance.save()
        else:
            print("class name missing")
    
    def do_show(self):
        """Print string represantation of an instance based on the class name and id."""
        pass

    def do_destroy(self):
        """Delete an innstance based on the class name and id."""
        pass

    def do_all(self):
        """Print all string represantation of all instaces."""
        pass

    def do_update(self):
        """Update an instance based on the class name and id by adding or updting attribute."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
