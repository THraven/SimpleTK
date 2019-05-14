#!/usr/bin/python

"""this file contains all functions for the desktop app"""

class SimpleTk():
    """the container class for all functions used"""

    def InitButton(self, name="button%s" % len(self.button), text="", command=None):
        """this is for the easy making of buttons in the app.
        and will store some stuff in the """
        if name == None:
            name = "button%s" % len(self.button)
        DisplayText = tk.StringVar()
        DisplayText.set(text)
        ButtonInctence = tk.Button(self.window, textvariable=DisplayText, command=command)
        self.button.update({name: {"button": ButtonInctence,
                                    "text": DisplayText}})
        self.button[name]["button"].pack()

    def InitLabel(self, name=None, text=None):
        """this is for the easy making of labels in the app.
        it will store this such as name and text"""
        if name == None:
            name = "label%s" % len(self.label)
        DisplayText = tk.StringVar()
        if not type(text) == type(DisplayText):
            DisplayText.set(text)
        else:
            DisplayText = text
        LabelInctence = tk.Label(self.window, textvariable=DisplayText)
        self.label.update({name: {"label": LabelInctence,
                                    "text": DisplayText}})
        self.label[name]["label"].pack()
