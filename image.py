from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from datetime import datetime
import json
import time
#import data
import hashlib

with open('Technitians.json','r+') as File_Technitians_list:
    Technitian_list=json.load(File_Technitians_list)

print(Technitian_list)


windows=Tk()
Image_file=Image.open("Cabinets_tw.jpg")
Image_file.resize((50,50),Image.ANTIALIAS)
im=ImageTk.PhotoImage(Image_file)
Image_disp=Label(image=im,width=500,height=500)
Image_disp.pack()

windows.mainloop()