import time
import tkinter as tk
from datetime import datetime

windows=tk.Tk()
windows.geometry('650x600')
windows.title('time')
frame=tk.Frame(master=windows, width=650, height=600)

def focusToSN(event):
    print("it works")

now=datetime.now()
Record=tk.Label(master=frame,font=("arial",16),text=now.strftime("%H:%M:%S"))
Record.place(x=10,y=10)
Data_input=tk.Entry(master=frame,font=("arial",16),width=30)
Data_input.place(x=0,y=60)
Data_input.bind('<Return>',focusToSN)


def update():
    now=datetime.now()
    Record=tk.Label(master=frame,font=("arial",16),text=now.strftime("%H:%M:%S"))
    Record.place(x=10,y=10)
    windows.after(1000, update)

update()
frame.pack()
windows.mainloop()
