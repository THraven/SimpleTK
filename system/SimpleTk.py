#!/usr/bin/python

"""this file contains all functions for the desktop app"""

import Tkinter as tk

class SimpleTk():
    """the container class for all functions used"""

    window = tk.Tk()
    button = {}
    label = {}
    entry = {}
    text = {}

    def textcheck(f):
        """this will check if the text given is a stringvar or not"""
        def wrapper(*args, **kwargs):
            DisplayText = tk.StringVar()
            if "textvariable" in kwargs and not type(kwargs["textvariable"]) == type(DisplayText):
                DisplayText.set(kwargs["textvariable"])
                kwargs["textvariable"] = DisplayText
            return f(*args, **kwargs)
        return wrapper

    @textcheck
    def InitButton(self, name=None, **kwargs):
        """this is for the easy making of buttons in the app.
        and will store some stuff in the """
        # checking if the name is given, if not it will just generate a name
        if name == None:
            name = "button%s" % len(self.button)
        ButtonInctence = tk.Button(self.window, **kwargs)
        self.button.update({name: {"object": ButtonInctence}})
        self.button[name].update(kwargs)
        self.button[name]["object"].pack()

    @textcheck
    def InitLabel(self, name=None, **kwargs):
        """this is for the easy making of labels in the app.
        it will store data such as name and text"""
        if name == None:
            name = "label%s" % len(self.label)
        LabelInctence = tk.Label(self.window, **kwargs)
        self.label.update({name: {"object": LabelInctence}})
        self.label[name].update(kwargs)
        self.label[name]["object"].pack()

    @textcheck
    def InitEntry(self, name=None, **kwargs):
        """this is for the easy making of entry forms in the app.
        it will store data such as name and text"""
        if name == None:
            name = "entry%s" % len(self.entry)
        EntryInctence = tk.Entry(self.window, **kwargs)
        self.entry.update({name: {"object": EntryInctence}})
        self.entry[name].update(kwargs)
        self.entry[name]["object"].pack()
