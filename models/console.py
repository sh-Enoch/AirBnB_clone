#!usr/bin/python3
"""Entry point of the interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Define class HBNBCommand."""

    prompt = "(hbnb)"

    def do_quit(self):
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
                    print("{}".format(cmd[3:]), end="")
            print()
            print()

    def do_EOF(self):
        """Exit program."""
        print()
        return True

    def emptyline(self):
        """Shouldn't execute anything on new line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
