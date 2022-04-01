from tkinter import * 
from PIL import Image,ImageTk
from Home import *
import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Manorama#4269",
    database="school_dbms"
    )

global username
global password

username = StringVar()
password = StringVar()


window = Tk()
window.title("LOGIN PAGE")
window.geometry("1920x1080")
window.config(bg="#f6f6f6")

# def verify():
#     if e1.get()=="" or e2.get()=="":
#         empty()
    
#     elif e1.get()== "Admin" or e2.get()=="Admin@1234":
#         window.destroy()
#         home()
#     elif e1.get()== "Teacher" or e2.get()=="Teacher@1234":
#         window.destroy()
#         home()
#     elif e1.get()== "Student" or e2.get()=="Student@1234":
#         window.destroy()
#         home()
#     elif e1.get()== "Developer" or e2.get()=="developer@1234":
#         window.destroy()
#         home()
#     else: 
#         error()

    #If the entry box is empty 
def empty():
    emp1=Label(text="Please Enter All the Details",fg="Black")
    emp1.place(x=42,y=230)
    emp1.config(bg="#f6f6f6",fg="#6177FE",font=('Lucida Console',12))
    print(emp1)
    return    
    #If the entered info is incorrect
def error():
    ero=Label(text="Username or Password is Incorrect")
    ero.place(x=42,y=230)
    ero.config(bg="#f6f6f6",fg="#6177FE",font=('Lucida Console',12))
    print(ero)
    return

    


#Bg img
image = Image.open('media/hbg.jpg')
image = image.resize((1000,  700), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
my_lbl = Label(image = my_img) 
my_lbl.pack()

#Login entry
e1 = Entry(text="",bg='#EFEFEF',relief="flat")
e1.place(x=45,y=300,height=50,width=255)

#Password label
l2 = Label(text="Password",bg="#f6f6f6", font=('Lucida Console', 11))
l2.place(x=30,y=390,height=30,width=100)
        
#Password entry
e2 = Entry(show ="*",bg="#EFEFEF",relief="flat")
e2.place(x=45,y=420,height=50,width=255)

#Forgot_pwd Button
f_pwd = Button(text="forgot password?",bd=0, fg="Black",underline=0 ,relief='flat', cursor="hand2",bg="#f6f6f6",command=lambda:fps(window))
f_pwd.place(x=200,y=475)




#Login label
l1 = Label(text="Username",bg="#f6f6f6", font=('Lucida Console', 11))
l1.place(x=30,y=270,height=30,width=100)


#Verifying the entered info from the user.
def login():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM login WHERE BINARY username = '%s' AND BINARY password = '%s'" % (username.get(),password.get())

    mycursor.execute(sql)

    if mycursor.fetchone():
        window.destroy()
        home()
    else:
        error()

#Submit Button
submit = Button(text="Login",command=login,bd=0,bg="#7028c6",fg="#FFFFFF",relief="flat",font=('Lucida Console', 11))
submit.place(x=45,y=530,height=45,width=150)



window.state('zoomed')
window.mainloop()



