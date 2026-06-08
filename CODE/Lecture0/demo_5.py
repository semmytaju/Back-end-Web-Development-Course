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

# define width, height and coordinates (frame size)
window.geometry('350x200')

# Add label
lbl = Label(window, text="Add new user: ")
lbl.grid(column=0, row=0)

# Add button
btn = Button(window, text="Click Me", bg="orange", fg="red")
btn.grid(column=1, row=0)

# infinite loop used to run the application
window.mainloop()

