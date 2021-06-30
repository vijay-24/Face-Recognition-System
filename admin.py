import cv2
import tkinter as tk
from tkinter import *
from tkinter import ttk
# import ttk
# from ttk import Frame
# import faces as faces
from PIL import Image, ImageTk
import numpy as np
import cv2
from tkinter import messagebox
from datetime import date
import time
from PIL import Image, ImageDraw, ImageFont
import face_recognition
import face_recognition_models
import dlib
import numpy as np
import mysql.connector
import tksheet
import os

white 		= "#ffffff"
lightBlue2 	= "#adc5ed"
font 		= "Constantia"
fontButtons = (font, 12)
maxWidth  	= 800
maxHeight 	= 480


mainWindow = tk.Tk()
mainWindow.configure(bg=lightBlue2)
mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))
mainWindow.geometry("1300x600")

sheet = tksheet.Sheet(mainWindow)
sheet.pack()
sheet.place(x=50,y=80)
# sheet.columnconfigure(["sid"])
# sheet.set_sheet_data([[f"{ri+cj}" for cj in range(4)] for ri in range(1)])
sheet.headers(["Employee Id","Name","Employee Image"])
# sheet.set_sheet_data([["a","b","C"],["a","b","C"]])
# sheet.set_sheet_data([[i+1,i+2,i+3]for i in range(10)])


# table enable choices listed below:

sheet.enable_bindings(("single_select",

                       "row_select",

                       "column_width_resize",

                       "arrowkeys",

                       "right_click_popup_menu",

                       "rc_select",

                       "rc_insert_row",

                       "rc_delete_row",

                       "copy",

                       "cut",

                       "paste",

                       "delete",

                       "undo",

                       "edit_cell"))


Atd_sheet = tksheet.Sheet(mainWindow)
Atd_sheet.place(x=590,y=80)
# sheet.columnconfigure(["sid"])
# sheet.set_sheet_data([[f"{ri+cj}" for cj in range(4)] for ri in range(1)])
Atd_sheet.headers(["Employee Id","Name","Date and Time"])
# Atd_sheet.set_sheet_data([["a","b","C"],["a","b","C"]])
# Atd_sheet.set_sheet_data([[i+1,i+2,i+3]for i in range(10)])

# table enable choices listed below:

Atd_sheet.enable_bindings(("single_select",

                       "row_select",

                       "column_width_resize",

                       "arrowkeys",

                       "right_click_popup_menu",

                       "rc_select",

                       "rc_insert_row",

                       "rc_delete_row",

                       "copy",

                       "cut",

                       "paste",

                       "delete",

                       "undo",

                       "edit_cell"))




image = Image.open("D:\\Face_Python\\images\\Pic_vk2021_05_11_21_15_37.jpg")
resize_image = image.resize((200,200))
img = ImageTk.PhotoImage(resize_image)


label = tk.Label(mainWindow,background="red",image=img)
label.place(x=1100,y=100)


def Emp_Detail():
    print('ins')
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="vk"
    )
    cursor = conn.cursor()
    # sql = "INSERT INTO `t1`(`name`,img) VALUES ('sam','Pic_vk2021_05_11_21_15_37.jpg')";
    # cursor.execute(sql)
    sql= "select * from t1"
    cursor.execute(sql)
    # print(cursor.fetchall())
    # for i in cursor.fetchall():
    #     print(i[0],i[1],i[2])
    #     print("D:\\Face_Python\\images\\"+i[2])
    #     image = Image.open("D:\\Face_Python\\images\\"+i[2])
    #     resize_image = image.resize((200, 200))
    #     img = ImageTk.PhotoImage(resize_image)
    #     label.configure(image=img)
    #     # label = tk.Label(mainWindow, background="red", image=img)
    #     # label.place(500,500)
    #     messagebox.showinfo("good")
    sheet.set_sheet_data([[i[0], i[1], i[2]] for i in cursor.fetchall()])
    conn.close()


def Atd_Details():
    print("attandance detail")
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="vk"
    )
    file = 'Pic_vk2021_05_11_21_15_37.jpg'
    cursor = conn.cursor()
    # sql = "INSERT INTO `t1`(`name`,img) VALUES ('sss','"+file+"')";
    # cursor.execute(sql)
    sql = "select * from at"
    cursor.execute(sql)
    # for i in cursor.fetchall():
    #     print(i)
    Atd_sheet.set_sheet_data([[i[0], i[1], i[2]] for i in cursor.fetchall()])
    conn.close()


def recognize_window():
    mainWindow.destroy()
    os.system('main.py')

closeButton = Button(mainWindow, text = "CLOSE", font = fontButtons, bg = "Red", width = 20, height= 1)
closeButton.configure(command= lambda: mainWindow.destroy())
closeButton.place(x=1130,y=40)

Emp_lbl=tk.Label(mainWindow,text="Employee Details ",height=1,width=18,bg=lightBlue2,font =('times', 18, ' bold '))
Emp_lbl.place(x=90,y=30)

Emp_Button = Button(mainWindow, text = "Show Employee Details", font = fontButtons, bg = white, width = 20, height= 1,command= Emp_Detail)
Emp_Button.place(x=120, y=400)


Atd_lbl=tk.Label(mainWindow,text="Employee Attandance Details ",height=1,width=28,bg=lightBlue2,font =('times', 18, ' bold '))
Atd_lbl.place(x=590,y=30)

Atd_Button = Button(mainWindow, text = "Show Employee Attandance Details", font = fontButtons, bg = white, width = 30, height= 1,command= Atd_Details)
Atd_Button.place(x=690, y=400)

Cam_Button = Button(mainWindow, text = "Recognize window", font = fontButtons, bg = white, width = 30, height= 1,command= recognize_window)
Cam_Button.place(x=390, y=500)

mainWindow.mainloop()
