#-*- coding: utf-8 -*-
import sys
import importlib
import cv2
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog

# Set Current Working Directory
work_dir = "D:/UNKLAB CLASSES/UNKLAB TEACHING/CLASS/Framework Programming/CODE/Lecture17";

# Function to read image path
def selectPath():
    global path_
    path_ = filedialog.askopenfilename()
    path.set(path_)
  
# Handle Open CV when click button
def detectFaceImage():
    try:
        # github Obtaining trained face parameter data
        face_cascade = cv2.CascadeClassifier('{0}/cascades/haarcascade_frontalface_default.xml'.format(work_dir))

        # Read pictures
        image = cv2.imread(path_)

        #Convert to Grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detecting faces in pictures
        faces = face_cascade.detectMultiScale( gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5), flags=cv2.IMREAD_GRAYSCALE)

        if(len(faces)==0):
            tkinter.messagebox.showerror('Error Message', 'No face recognized, please choose a clearer picture.')

        print("System recognized {0} faces.".format(len(faces)))

        # faces [x-coordinate, p-coordinate, width, and length of the upper left corner]
        for (x, y, w, h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+w),(255,245,0),1)
        if (len(faces) > 0):
            cv2.imshow("Recognized {0} faces".format(len(faces)), image)
        
        # Key press handling
        cv2.waitKey(0)
    except:
        tkinter.messagebox.showerror('Error Message', 'Please select the correct picture file.')
     
        
# Design Python GUI
#importlib.reload(sys)

window = tk.Tk()
window.title('Face Detection System')

fm1 = tk.Frame(window)
fm2 = tk.Frame(window)

path = tk.StringVar()

Ltop=tk.Label(fm1,text="Please select a picture path")
B1=tk.Button(fm2, text = "Select image file: ", command = selectPath)
E1=tk.Entry(fm2, textvariable = path, bd=5)
B2=tk.Button(fm2, text = "Detect Face", command = detectFaceImage)

Ltop.pack(side = tk.TOP)
B1.pack(side = tk.LEFT)
E1.pack(side = tk.LEFT)
B2.pack(side = tk.LEFT)

fm1.pack(side = tk.TOP)
fm2.pack(side = tk.TOP)

#Get the screen width & height
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()

ww = 300
wh = 100

#Window width and height 100
x = (sw-ww) / 2
y = (sh-wh) / 3
window.geometry("%dx%d+%d+%d" %(ww,wh,x,y))

# infinite loop used to run the application
window.mainloop()
