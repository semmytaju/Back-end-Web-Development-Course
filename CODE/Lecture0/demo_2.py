# -*- coding: utf-8 -*-
"""
    Created : Mon Jun 21 06:15:12 2021
    @author : SWT
"""

# import Tkinter package 
from tkinter import *

# create the main window (container)
window = Tk()

# Add any number of widgets to the main window
# set windows title
window.title("Welcome to Python GUI")

# create a label using the label class
lbl = Label(window, text="Hello 1 : Text add label")

# set position on form and give it the location
lbl.grid(column=0, row=0)

# set label font size
lbl2 = Label(window, text="Hello 2 : font size", font=("Arial Bold", 50))

# set position on form and give it the location
lbl2.grid(column=1, row=5)

# infinite loop used to run the application
window.mainloop()

