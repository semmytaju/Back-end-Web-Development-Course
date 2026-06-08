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

# add ComboBox
combo = Combobox(window)
# add items in combobox
combo['values']= (1, 2, 3, 4, 5, "Text")

# set the selected item
combo.current(1) 

combo.grid(column=0, row=0)

# infinite loop used to run the application
window.mainloop()

