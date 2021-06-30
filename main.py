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
import os



face_cascade = cv2.CascadeClassifier('D:\\lib for python\\youtuber method\\facerecog\\myenvpy\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:\\lib for python\\youtuber method\\facerecog\\myenvpy\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')


white 		= "#ffffff"
lightBlue2 	= "#adc5ed"
font 		= "Constantia"
fontButtons = (font, 12)
maxWidth  	= 800
maxHeight 	= 480

#Graphics window
mainWindow = tk.Tk()
mainWindow.configure(bg=lightBlue2)
mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))
mainWindow.geometry("1300x500")
# mainWindow.resizable(0,0)
# mainWindow.overrideredirect(1)

mainFrame = Frame(mainWindow,borderwidth = 1,highlightcolor="green",highlightbackground="green")
mainFrame.place(x=20, y=20)

fram = ImageTk.PhotoImage(file='D:\\people.jpg')
#Capture video frames
lmain = tk.Label(mainFrame,background="red")
lmain.grid(row=0, column=0)
myfrm = Frame(mainWindow, width=200 , height=200,  bg="Blue")
# myfrm.place(x=820, y=20)
# myfrm=frame

# cap = cv2.VideoCapture('F:\\movies\\video songs\\Adada Mazhaida.mp4')
cap = cv2.VideoCapture(0)



obama=face_recognition.load_image_file("D:\\Face_Python\\images\\obama.jpg")
obama_enc=face_recognition.face_encodings(obama)[0]
biden = face_recognition.load_image_file("D:\\Face_Python\\images\\biden.jpg")
biden_en = face_recognition.face_encodings(biden)[0]
kum = face_recognition.load_image_file("D:\\Face_Python\\images\\Pic_kuman2021_05_13_11_11_22.jpg")
kum_enc = face_recognition.face_encodings(kum)[0]
vi = face_recognition.load_image_file("D:\\Face_Python\\images\\Pic_vk2021_05_11_21_15_37.jpg")
vi_enc = face_recognition.face_encodings(vi)[0]


# temp=face_recognition.face_locations(vi)
# temp_en=face_recognition.face_encodings(temp)[0]
# print(temp_en)
enc=[]
enc.append(biden_en)
enc.append(obama_enc)
enc.append(kum_enc)
enc.append(vi_enc)

name=[]
name.append('Biden')
name.append('obama')
name.append('kuman')
name.append('vk')
# for i in range(4):
# 	print(name[i],i,enc[i])
k=[]
k.append(4)
def show_frame():
	ret, frame = cap.read()
	frame = cv2.flip(frame,1)
	cv2.imwrite('D:\\Face_Python\\images\\frme.jpg', frame)
	unknown = face_recognition.load_image_file("D:\\Face_Python\\images\\frme.jpg")
	na = 'unknown person'
	na=check_face()
	i=0

	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

	# -----------------Face Recognition Part______________________________________
	faces = face_cascade.detectMultiScale(
		cv2image,
		scaleFactor=1.2,
		minNeighbors=5,
		minSize=(20, 20)
    )
	for (x, y, w, h) in faces:
		cv2.rectangle(cv2image, (x, y), (x + w, y + h), (0, 0, 0), 2)
		roi_gray = cv2image[y:y + h, x:x + w]
		roi_color = cv2image[y:y + h, x:x + w]
		cv2.putText(cv2image, na, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 255), 1)


	img = Image.fromarray(cv2image).resize((760, 400))
	imgtk = ImageTk.PhotoImage(image = img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)


def snap():
	_, frame = cap.read()
	frame = cv2.flip(frame, 1)
	date_string = time.strftime("%Y_%m_%d_%H_%M_%S")


	cv2.imwrite('D:\Face_Python\images\Pic_'+str(txt_new_emp_name.get())+date_string+'.jpg', frame)

	# mainWindow.myfrm = ImageTk.PhotoImage(file='D:\pythonProject\images\Pic_'+str(name())+date_string+'.jpg')
	# print("snaped")
	messagebox.showinfo("Information", "Snaped")
	# t=face_recognition.load_image_file(pa)
	# t_en=face_recognition.face_encodings(t)[0]
	# enc.append(t_en)
	# name.append(txt_new_emp_name.get())
	# k[0]=k[0]+1

	file="Pic_"+str(txt_new_emp_name.get())+date_string+'.jpg'
	na=str(txt_new_emp_name.get())
	print(file)
	#--------------------------------------------
	conn = mysql.connector.connect(
		host="localhost",
		user="root",
		password="",
		database="vk"
	)
	cursor = conn.cursor()
	sql = "INSERT INTO `t1`(`name`,img) VALUES ('"+na+"','"+file+"')"
	cursor.execute(sql)
	# sql = "select * from t1"
	# cursor.execute(sql)
	# for i in cursor.fetchall():
	# 	print(i)
	conn.close()




# vk = ImageTk.PhotoImage(file='D:\\pythonProject\\images\\Pic_asfd2021_04_18_21_10_58.jpg')
def test():
	print("good")
	# cv2.imread('D:\\Face_Python\\images')
	# test_img=face_recognition.load_image_file("D:\\Face_Python\\images\\Pic_kuman2021_05_13_11_11_22.jpg")
	# real_img= face_recognition.load_image_file("D:\\Face_Python\\images\\Pic_vk2021_05_11_21_15_37.jpg")


	# test_img = face_recognition.load_image_file("D:\\Face_Python\\images\\obama.jpg")
	# test_img_en = face_recognition.face_encodings(test_img)[0]

	# real_img = face_recognition.load_image_file("D:\\Face_Python\\images\\biden.jpg")
	# real_img = cv2.cvtColor(real_img, cv2.COLOR_BGR2RGBA)
	# real_img1=face_recognition.face_locations(real_img)
	# real_img_en = face_recognition.face_encodings(real_img)[0]
	#
	# img1=face_recognition.load_image_file("D:\\Face_Python\\images\\Pic_vk2021_05_11_21_15_37.jpg")
	# img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGBA)
	# img1_en=face_recognition.face_encodings(img1)[0]
	# img2=face_recognition.load_image_file("D:\\Face_Python\\images\\human_2.jpg")
	# img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGBA)
	# img2_en=face_recognition.face_encodings(img2)[0]
	# fac_loc=face_recognition.face_locations(real_img])[0]
	# enc_face=face_recognition.face_encodings(real_img)[0]
	# cv2.rectangle(real_img, (x, y), (x + w, y + h), (0, 0, 0), 2)
	#
	# fac_loc_test=face_recognition.face_locations(test_img)[0]
	# enc_face_test=face_recognition.face_encodings(test_img)[0]
	# cv2.rectangle(test_img, (x, y), (x + w, y + h), (0, 0, 0), 2)
	# temp=[img1,img2,real_img_en,test_img]
	# temp.append(img1)
	# temp.append(img2)
	# # temp.append(real_img_en)
	# temp.append(test_img)


	# face_detector = dlib.get_frontal_face_detector()
	# for i in range(3):
	# 	print(i)
	# results = face_recognition.compare_faces([test_img_en],test_img_en)
	# print("my results",results)
	#
	# cv2.waitKey(0)

def check_face():
	name="Unknown Name"
	# print('check')
	try:
		# "D:\\Face_Python\\images\\obama.jpg"
		img=face_recognition.load_image_file("D:\\Face_Python\\images\\frme.jpg")
		img_en = face_recognition.face_encodings(img)[0]
		# ------------------------------------------------------
		conn = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database="vk"
		)
		cursor = conn.cursor()
		# sql = "INSERT INTO `t1`(`name`,img) VALUES ('sam','" + file + "')"
		sql = "Select * from t1"
		cursor.execute(sql)
		for i in cursor.fetchall():
			file="D:\\Face_Python\\images\\" + i[2]
			# print(file)
			known = face_recognition.load_image_file(file)
			known_enc = face_recognition.face_encodings(known)[0]
			matches = face_recognition.compare_faces([known_enc], img_en)
			# print(matches)
			if (matches[0]== True):
				name = i[1]
				Atd_Marking(name)
				return name

		conn.close()

	except IndexError:
		{}
	return name


def Atd_Marking(name):
	date_string = time.strftime("%Y_%m_%d_%H_%M_%S")
	conn = mysql.connector.connect(
		host="localhost",
		user="root",
		password="",
		database="vk"
	)
	cursor = conn.cursor()
	sql = "INSERT INTO at(nam,d_t) VALUES ('"+name+"','" + date_string + "')"
	cursor.execute(sql)
	conn.close()


def Admin_window():
	if txt_Admin_Id.get()=='a' and txt_Admin_pass.get()=='a':
		cap.release()
		mainWindow.destroy()
		os.system('Admin_View.py')
	else:
		messagebox.showinfo("Alert", "Admin Id or password are Wrong!! ")


closeButton = Button(mainWindow, text = "CLOSE", font = fontButtons, bg = white, width = 20, height= 1)
closeButton.configure(command= lambda: mainWindow.destroy())
closeButton.place(x=270,y=430)

SaveButton = Button(mainWindow, text = "Save", font = fontButtons, bg = white, width = 20, height= 1,command= snap)
# SnapButton.configure(command= snap: mainWindow.destroy())
SaveButton.place(x=850, y=350)

dbButton = Button(mainWindow, text = "Admin_window", font = fontButtons, bg = white, width = 20, height= 1,command= Admin_window)
dbButton.place(x=1050, y=350)

testButton = Button(mainWindow, text = "Compare", font = fontButtons, bg =white, width = 20, height= 1,command= test)
testButton.place(x=860,y=430)

lbl_Admin_id=tk.Label(mainWindow,text="Admin Id     :",height=1,width=12,bg="lightBlue2",font =('times', 12, ' bold '))
lbl_Admin_id.place(x=800,y=250)

lbl_Admin_pass=tk.Label(mainWindow,text="Password    :",height=1,width=12,bg="lightBlue2",font =('times', 12, ' bold '))
lbl_Admin_pass.place(x=800,y=280)

lbl_name=tk.Label(mainWindow,text="New Employee Name :",height=1,width=18,bg="lightBlue2",font =('times', 12, ' bold '))
lbl_name.place(x=800,y=310)
# lbl.place(in_=frame, relx=0.1,rely=0.35, anchor="nw")
txt_Admin_Id = ttk.Entry(mainWindow, width = 17)
txt_Admin_Id.place(x=970,y=250)

txt_Admin_pass = ttk.Entry(mainWindow, width = 17)
txt_Admin_pass.place(x=970,y=280)

txt_new_emp_name = ttk.Entry(mainWindow,width=17)
txt_new_emp_name.place(x=970,y=310)



photo = Image.open("D:\\Face_Python\\images\\admin.jpg").resize((250, 200))
photo = ImageTk.PhotoImage(photo)
lbl_snap=tk.Label(mainWindow,image=photo)
lbl_snap.place(x=820, y=20)


show_frame()  #Display
mainWindow.mainloop()  #Starts GUI
