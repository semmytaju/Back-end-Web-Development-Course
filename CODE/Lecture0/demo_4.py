# -*- coding: utf-8 -*-
"""
    Created : Mon Jun 21 06:15:12 2021
    @author : SWT
"""

#Import the tkinter library
from tkinter import *

#Create an instance of tkinter frame
window = Tk()

# set windows title
window.title("Welcome to Python GUI")

#Set the geometry
window.geometry("600x250")

window.eval('tk::PlaceWindow . center')

# infinite loop used to run the application
window.mainloop()

