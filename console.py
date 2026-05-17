#!/usr/bin/python3
"""Entry point of the AirBnB clone command interpreter."""
import cmd
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def emptyline(self):
        """Do nothing on an empty input line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the interpreter when EOF (Ctrl-D) is reached."""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of a class, save it, and print its id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        cls = HBNBCommand.classes.get(args[0])
        if cls is None:
            print("** class doesn't exist **")
            return
        instance = cls()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, arg):
        """Delete an instance based on its class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Print all string representations, optionally filtered by class."""
        args = shlex.split(arg)
        if args and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        items = []
        for key, obj in storage.all().items():
            if not args or key.startswith(args[0] + "."):
                items.append(str(obj))
        print(items)

    def do_update(self, arg):
        """Update an instance attribute and save the change."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr, value = args[2], args[3]
        if attr in ("id", "created_at", "updated_at"):
            return
        current = getattr(obj, attr, None)
        if current is not None:
            try:
                value = type(current)(value)
            except (TypeError, ValueError):
                pass
        setattr(obj, attr, value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
