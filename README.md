# SimpleTk framework

A framework for the ease of use of python's de facto standard GUI library, Tkinter, and simplify the use of all it's systems.

## changelog
in the project
* moved decorators.py to folder **system/**
* moved SimpleTk.py to folder **system/**

in decorators.py <br>
* removed textcheck and moved it in to the SimpleTk class

in SimpleTk.py
* updated from a rigid argument system to useing kwargs this allows the system to
take any arguments given and not crash
* now the storing varibles store the entire kwargs dict so it doesn't matter what you give you can always reach it
* added InitEntry method
* rewrote some of the code to accommodate the kwargs changes
* added textcheck method to the SimpleTk class

in main.py
* added example code for current build
