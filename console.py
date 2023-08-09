#!/usr/bin/python3
""" import cmd"""
import models
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
        if key in open(BaseModel().__file_path, "r"):
            print(key)
        else:
            print("** no instance found **")    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
