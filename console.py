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
            args_len = len(arg)
            if args_len == 1:
                class_name = arg[0]
                if class_name == "BaseModel":
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            else:
                class_name = arg[0]
                instance_id = arg[1]
                if class_name != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    key = "{}.{}".format(class_name, instance_id)
                    try:
                        del storage._FileStorage__objects[key]
                        storage.save()
                    except KeyError:
                        print("** no instance found **")
            

    def do_all(self, arg):
        """Print all String rep of all instances."""
        if arg:
            if arg[0] != "BaseModel":
                print("** class doesn't exist **")
        else:
            for key, value in storage._FileStorage__objects.items():
                print(storage._FileStorage__objects[key])


    def do_update(self, lines):
        """Updatesan insatance based on the class name and id."""
        if lines:
            arg = lines.split()
            num_args =  len(arg)
            class_name = arg[0]
            if class_name != "BaseModel":
                print("** class doesn't exist **")
                return

            if num_args < 2:
                print("** instance id missing **")
                return
            else:
                #id present
                instance_id = arg[1]

            if num_args < 3:
                # no attribute name
                print("** attribute name missing **")
                return
            else:
                # attribute name
                attribute_name = arg[2]

            if num_args < 4:
                # no attribute value
                print("** value missing **")
                return
            else:
                attribute_value = arg[3]

            key = "{}.{}".format(class_name, instance_id)
            if key in storage._FileStorage__objects.keys():
                setattr(class_name, attribute_name, attribute_value)
                storage.save()
            else:
                print("** no instance found")
                return
        else:
            print("** class name missing **")
        
if __name__ == "__main__":
    HBNBCommand().cmdloop()
