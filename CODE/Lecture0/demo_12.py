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

# add Message dialog
def clicked():
    messagebox.showinfo('Message title', 'Message content')

# add botton
btn = Button(window,text='Click here', command=clicked)
btn.grid(column=0,row=0)

# infinite loop used to run the application
window.mainloop()

