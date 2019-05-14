#!/usr/bin/python

"""this file contains all functions for the desktop app"""

class SimpleTk():
    """the container class for all functions used"""

    def InitButton(self, name=None, text="", command=None):
        """this is for the easy making of buttons in the app.
        and will store some stuff in the """
        # checking if the name is given, if not it will just generate a name
        if name == None:
            name = "button%s" % len(self.button)
        DisplayText = tk.StringVar()
        DisplayText.set(text)
        ButtonInctence = tk.Button(self.window, textvariable=DisplayText, command=command)
        self.button.update({name: {"button": ButtonInctence,
                                    "text": DisplayText}})
        self.button[name]["button"].pack()
