#!/usr/bin/python

"""this file contains all functions for the desktop app"""

import Tkinter as tk
from PIL import Image, ImageTk

class vars():
    """the goal of this class is to contain all the propertys and global varibles
    the SimpleTk class uses."""

    image = {}
    button = {}
    label = {}
    entry = {}
    frame = {}
    text = {}

    @property
    def window(self):
        """contains the window """
        if hasattr(self, "_window"):
            return self._window
        self._window = tk.Tk()
        return self._window

    @window.setter
    def window(self, value):
        self._window = value

class SimpleTk(vars):
    """the container class for all functions used"""

    def precheck(f):
        """this will check if the text given is a stringvar or not"""
        def wrapper(*args, **kwargs):
            if not "window" in kwargs:
                kwargs["window"] = args[0].window
            else:
                args[0].window
            DisplayText = tk.StringVar()
            if "textvariable" in kwargs and not type(kwargs["textvariable"]) == type(DisplayText):
                DisplayText.set(kwargs["textvariable"])
                kwargs["textvariable"] = DisplayText
            return f(*args, **kwargs)
        return wrapper

    @precheck
    def InitButton(self, window=None, name=None, **kwargs):
        """this is for the easy making of buttons in the app.
        and will store some stuff in the """
        # checking if the name is given, if not it will just generate a name
        if name == None:
            name = "button%s" % len(self.button)
        ButtonInctence = tk.Button(window, **kwargs)
        self.button.update({name: {"object": ButtonInctence}})
        self.button[name].update(kwargs)
        self.button[name]["object"].pack()

    @precheck
    def InitLabel(self, window=None, name=None, **kwargs):
        """this is for the easy making of labels in the app.
        it will store data such as name and text"""
        if name == None:
            name = "label%s" % len(self.label)
        LabelInctence = tk.Label(window, **kwargs)
        self.label.update({name: {"object": LabelInctence}})
        self.label[name].update(kwargs)
        self.label[name]["object"].pack()

    @precheck
    def InitImage(self, window=None, name=None, **kwargs):
        """This uses labels to display images"""
        if name == None:
            name = "image%s" % len(self.image)
        load = Image.open(kwargs["image"])
        render = ImageTk.PhotoImage(load)
        kwargs['image'] = render
        ImageInctence = tk.Label(window, **kwargs)
        self.image.update({name: {"object": ImageInctence}})
        self.image[name].update(**kwargs)
        self.image[name]["object"].pack()

    @precheck
    def InitEntry(self, window=None, name=None, **kwargs):
        """this is for the easy making of entry forms in the app.
        it will store data such as name and text"""
        if name == None:
            name = "entry%s" % len(self.entry)
        EntryInctence = tk.Entry(window, **kwargs)
        self.entry.update({name: {"object": EntryInctence}})
        self.entry[name].update(kwargs)
        self.entry[name]["object"].pack()

    @precheck
    def InitFrame(self, window=None, name=None, side=tk.TOP, **kwargs):
        """this is for the easy creation of frames in the window,
        the frames will be stored in self.frame"""
        if name == None:
            name = "frame%s" % len(self.frame)
        FrameInctence = tk.Frame(window, **kwargs)
        self.frame.update({name: {"object": FrameInctence}})
        self.frame[name].update(kwargs)
        self.frame[name]["object"].pack(side=side)
