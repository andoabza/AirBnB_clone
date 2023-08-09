#!/usr/bin/python3
""" import cmd"""
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
