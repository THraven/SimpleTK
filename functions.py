#!/usr/bin/python

"""you can put all the functions for buttons, menus and other stuff here"""

from system import SimpleTk

class function(SimpleTk.SimpleTk):
    """put functions here"""

    def quit(self):
        self.window.destroy()
