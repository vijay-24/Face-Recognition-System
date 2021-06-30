# import main
import tkinter as tk
from tkinter import *
from  tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import numpy as np
import cv2
import os

mainWindow = tk.Tk()
mainWindow.configure(bg='lightblue2')
# mainWindow.geometry('%dx%d+%d+%d' % ('maxWidth','maxHeight,0,0))
mainWindow.geometry("350x400")

def check():
    if txt_Admin_Id.get()=='a' and txt_Admin_pass.get()=='a':
        print('fun exe')
        mainWindow.destroy()
        os.system('main.py')
    else:
        messagebox.showinfo("Information", "Your Crediential are Wrong!!")


photo = Image.open("D:\\Face_Python\\images\\admin.jpg").resize((250, 200))
photo = ImageTk.PhotoImage(photo)
lbl_snap=tk.Label(mainWindow,image=photo)
lbl_snap.place(x=40, y=20)

lbl_Admin_id=tk.Label(mainWindow,text="Admin Id     :",height=1,width=12,bg="lightBlue2",font =('times', 12, ' bold '))
lbl_Admin_id.place(x=20,y=250)

lbl_Admin_pass=tk.Label(mainWindow,text="Password    :",height=1,width=12,bg="lightBlue2",font =('times', 12, ' bold '))
lbl_Admin_pass.place(x=20,y=280)


txt_Admin_Id = ttk.Entry(mainWindow, width = 17)
txt_Admin_Id.place(x=190,y=250)
txt_Admin_pass = ttk.Entry(mainWindow, width = 17)
txt_Admin_pass.place(x=190,y=280)

SaveButton = Button(mainWindow, text = "Submit", font = 'fontButtons', bg = 'white', width = 20, height= 1,command=check)
# SnapButton.configure(command= snap: mainWindow.destroy())
SaveButton.place(x=70, y=350)


mainWindow.mainloop()
