# -*- coding: utf-8 -*-
"""
    Created : Mon Jun 21 06:15:12 2021
    @author : SWT
"""

# import Tkinter package 
from tkinter import *
from tkinter import Menu

# create the main window (container)
window = Tk()

# add any number of widgets to the main window
# set windows title
window.title("Welcome to Python GUI")

# define width, height and coordinates (frame size)
window.geometry('350x200')

# add menubar
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')

new_item.add_separator()

new_item.add_command(label='Edit')

menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

# infinite loop used to run the application
window.mainloop()

