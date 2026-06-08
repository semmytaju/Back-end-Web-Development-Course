# -*- coding: utf-8 -*-
"""
    Created : Mon Jun 21 06:15:12 2021
    @author : SWT
"""

# import Tkinter package 
from tkinter import *
from tkinter.ttk import *

# create the main window (container)
window = Tk()

# add any number of widgets to the main window
# set windows title
window.title("Welcome to Python GUI")

# define width, height and coordinates (frame size)
window.geometry('350x200')

# add radiobutton
rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)

# infinite loop used to run the application
window.mainloop()

