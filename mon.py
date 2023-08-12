#!/usr/bin/python3

# import modules used here -- sys is a very standard one
import sys
import cmd
class Name(cmd.Cmd):
    prompt = "$"
    def onecmd(self, s):
        if s in {"u"}:
            print('onecmd(%s)' % s)
        else:
            return cmd.Cmd.onecmd(self, s)
# Gather our code in a main() function
    def do_kill(self, s):
        if s in {"u"}:
            print('Hello')
  # Command line args are in sys.argv[1], sys.argv[2] ..
  # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  Name().cmdloop()
