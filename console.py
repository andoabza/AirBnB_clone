#!/usr/bin/python3
""" import cmd"""
import models
import json
import cmd
""" define the class"""
class HBNBCommand(cmd.Cmd):
    """ display text """
    prompt = "(hbnb)"
    """ for quit command """
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    """ define EOF """
    def do_EOF(self, line):
        """exit command to end the file"""
        return True
    def do_create(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
        elif arg  == "BaseModel":
            models.storage.save()
            print(models.base_model.BaseModel().id)
        else:
            print("** class doesn't exist **")
    """Prints the string representation of an instance based onthe class name and id"""
    def do_show(self, arg):
        new_line = arg.split()
        if not arg:
            print("** class name missing **")
            return

        if new_line[0] not in {"BaseModel"}:
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return
        data = models.storage.all()
        key = "{}.{}".format(new_line[0], new_line[1])
        if key in data.keys():
            obj = data[key]
            print(obj)

        else:
            print("** no instance found **")    

    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in {"BaseModel"}:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        data = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in data.keys():
            del data[key]
            models.storage._FileStorage__objects = data
            models.storage.save()
        else:
            print("** no instance found **")
    
    def do_all(self, arg):
 
        if len(arg) == 0 or arg  == "BaseModel":
            dat = models.base_model.BaseModel()
            print(f"[\"{dat}\"]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in {"BaseModel"}:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return

        obj = models.storage.all()[key]

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]

        if attr_name in ["id", "created_at", "updated_at"]:
            print("** Cannot update attribute {} **".format(attr_name))
            return

        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass

        setattr(obj, attr_name, attr_value)
        obj.save()





if __name__ == '__main__':
    HBNBCommand().cmdloop()
