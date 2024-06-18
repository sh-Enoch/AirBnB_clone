#!/usr/bin/python3
"""Command interpreter."""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage



class HBNBCommand(cmd.Cmd):
    """Entry point to the command interpreter."""
    
    classes = ["BaseModel"]

    prompt = "(hbnb) "

    def do_quit(self):
        """Exit program."""
        return True

    def do_help(self, arg):
        """Provide help to user."""
        pass

    def do_EOF(self, arg):
        """EOF to exit program."""
        return True

    def emptyline(self):
        """When an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel save it to JSON
        print id.
        """
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            arg = BaseModel()
            storage.new(arg)
            storage.save()
            print(arg.id)

    def do_show(self, lines):
        """Print string representation of  an instance bsed on the cass name and id."""
        if not lines:
            print("** class name missing **")
        if lines:
            arg = lines.split()
            if arg[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                if len(arg) != 2 or len(arg) < 2:
                    print("** instance id missing **")
                else:
                    class_name = arg[0]
                    instance_id = arg[1]
                    key = "{}.{}".format(class_name, instance_id)
                    a = storage._FileStorage__objects
                    try:
                        print(storage._FileStorage__objects[key])
                    except KeyError:
                        print("** no instance found **")


    def do_destroy(self, lines):
        """Delete an instance based on the class name and id."""
        if not lines:
            print("** class name missing **")
        if lines:
            arg = lines.split()
            print(len(arg))
            if len(arg) == 1:
                if arg[0] != "BaseModel":
                    print("** class doesn't exist **")

            else:
                instance_id = arg[1]
                if instance_id:
                    class_name =  arg[0]
                    instance_id = arg[1]
                    key = "{}.{}".format(class_name, instance_id)
                    try:
                        del storage._FileStorage__objects[key]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance not found **")

    def do_all(self, arg):
        """Print all String rep of all instances."""
        arg = arg.split()
        if arg:
            print(arg[0])
            if arg[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                for key, value in storage._FileStorage__objects.items():
                    print(storage._FileStorage__objects[key])
        else:
            for key, value in storage._FileStorage__objects.items():
                print(storage._FileStorage__objects[key])


    def do_update(self, lines):
        """Updatesan insatance based on the class name and id."""
        if lines:
            arg = lines.split()
            if arg[0] == "BaseModel":
                if len(arg) < 2:
                    print("** instance id missing **")
                else:
                    class_name = arg[0]
                    instance_id = arg[1]
                    key = "{}.{}".format(class_name, instance_id)
                    try:
                        storage._FileStorage__objects[key]
                        if arg[2]:
                            attribute_name = arg[2]
                            if arg[3]:
                                attribute_value = arg[3]
                                setattr(class_name, attribute_name, attribute_value)
                            else:
                                print("** value missing **")
                        else:   
                            print("** attribute name missing **")
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
