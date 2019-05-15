#!/usr/bin/python

from system import SimpleTk
import decorators

"""in this file will contain the main loop."""

class main(SimpleTk.SimpleTk):
    """this is the main class"""

    def __init__(self):
        self.HalloWorld()
        w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%sx%s+0+0" % (w, h))
        self.window.mainloop()

    def HalloWorld(self):
        """this is the hallo world window, say hi"""
        self.InitLabel(name="label1", textvariable="change me")
        self.InitEntry(name="entry1", textvariable=self.label["label1"]["textvariable"])
        self.InitButton(name="button1", text="exit", command=quit)

loop = main()
