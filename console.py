#!/usr/bin/python3
"""
Module consule.py
a cmd consule
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ a command interpreter class """
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True
    def do_quit(self, line):
        """Quit command to exit the program """
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()
