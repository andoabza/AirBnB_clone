#!/usr/bin/python3
""" import everything"""
import models
import json
import cmd
""" define the class"""
class HBNBCommand(cmd.Cmd):
    """ display text """
    prompt = "(hbnb) "
    name = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
    """ for quit command """
    def onecmd(self, s):
        objects = models.storage.all()
        mane = ["BaseModel.all()", "User.all()", "State.all()", "City.all()", "Place.all()", "Amenity.all()", "Review.all()"]
        coun = ["BaseModel.count()", "User.count()", "State.count()", "City.count()", "Place.count()", "Amenity.count()", "Review.count()"]
        if s in mane:
            var = [str(obj) for obj in objects.values() if type(obj).__name__ + ".all()" == s]
            val = str(var).replace("\"", '')
            print(val)
            return
        if s in coun:
            var = [str(obj) for obj in objects.values() if type(obj).__name__ + ".count()" == s]
            a = str(var).replace("[", '')
            b = a.replace("]", '')
            c = s.replace(".count()", '')
            x = b.count(c)
            print(x)
        else:
            return cmd.Cmd.onecmd(self, s)
    """ exit the cmd"""
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    """ define EOF """
    def do_EOF(self, line):
        """exit command to end the file"""
        return True
    """ create class instance"""
    def do_create(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
        elif arg in HBNBCommand.name:
            models.storage.save()
            if arg in {"User"}:
                print(models.user.User().id)
            if arg in {"BaseModel"}:
                print(models.base_model.BaseModel().id)
            if arg in {"State"}:
                print(models.state.State().id)
            if arg in {"City"}:
                print(models.city.City().id)
            if arg in {"Place"}:
                print(models.place.Place().id)
            if arg in {"Amenity"}:
                print(models.amenity.Amenity().id)
        else:
            print("** class doesn't exist **")
    """Prints the string representation of an instance based onthe class name and id"""
    def do_show(self, arg):
        new_line = arg.split()
        if not arg:
            print("** class name missing **")
            return

        if new_line[0] not in HBNBCommand.name:
            print("** class doesn't exist **")
            return

        if len(new_line) < 2:
            print("** instance id missing **")
            return
        data = models.storage.all()
        key = "{}.{}".format(new_line[0], new_line[1])
        if key in data.keys():
            obj = data[key]
            print(obj)

        else:
            print("** no instance found **")    
    """ delete specified class instance"""
    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in HBNBCommand.name:
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
    """ function print basedd on arg"""
    def do_all(self, arg):
        objects = models.storage.all()
        if arg:
            if arg not in HBNBCommand.name:
                print("** class doesn't exist **")
                return
            else:
                print([str(obj) for obj in objects.values() if type(obj).__name__ == arg])
        else:
            print([str(obj) for obj in objects.values()])

    """Updates an instance based on the class name and id"""
    def do_update(self, arg):
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in HBNBCommand.name:
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
