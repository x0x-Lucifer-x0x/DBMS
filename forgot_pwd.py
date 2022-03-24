
import tkinter
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from functions import qite
import time 

def pwd():

     root = Tk()
     root.title("Forgot Password")
     root.geometry("1920x1080")
     root.config(bg="#f6f6f6")

     def msg():
          if e1.get()=="" or len(e1.get())!= 9  :
               lb = Label(text="Invalid Gr Number.",bg="#f6f6f6",font=('Lucida Console',12))
               lb.place(x=450,y=430)
               
          elif len(e1.get())== 9:
               lb= Label(text="Your Request has been sent to the Admin.\n Please be patient.",bg="#f6f6f6",font=('Lucida Console',12))
               lb.place(x=320,y=430)
               root.update()
               time.sleep(3)
               qite(root)
          
          
          
     image = Image.open('finalfpwd1.jpg')
     image = image.resize((1000,  700), Image.ANTIALIAS)
     my_img = ImageTk.PhotoImage(image)
     my_lbl = Label(image = my_img) 
     my_lbl.pack()

     b1 = Button( root,text="Back",bg="#f6f6f6",command=lambda:qite(root),fg="Black",relief="flat",font=('Lucida Console', 20))
     b1.place(x=900,y=40,height=50,width=80)

     l1 = Label( root,text="Forgot Password",bg="#f6f6f6",fg="Black", font=('Lucida Console', 30))
     l1.place(x=292,y=20,height=110,width=500)

     l2 = Label( root,text="Enter your Admission Number ",bg="#f6f6f6",fg="Black", font=('Lucida Console', 18))
     l2.place(x=307,y=240,height="50",width="450")

     e1 = Entry( root,text="",bg='#EFEFEF',relief="flat")
     e1.place(x=375,y=295,height="50",width="300")

     b2 = Button( root,text="CONTINUE",command=msg,bg="#7028c6",fg="#FFFFFF",relief="flat",font=('Lucida Console', 11))
     b2.place(x=450,y=355,height="40",width="160")


     root.state('zoomed')
     root.mainloop()

#pwd()

