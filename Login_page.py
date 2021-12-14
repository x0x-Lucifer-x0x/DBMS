from tkinter import * 
from PIL import Image,ImageTk
from forgot_pwd import *

class Login:
    def __init__(self, window):
        self.window = window
        self.window.title("LOGIN PAGE")
        self.window.geometry("1920x1080")
        self.window.config(bg="#f6f6f6")


        #Bg img
        self.image = Image.open('hbg.jpg')
        self.image = self.image.resize((1600,  850), Image.ANTIALIAS)
        self.my_img = ImageTk.PhotoImage(self.image)
        self.my_lbl = Label(image = self.my_img) 
        self.my_lbl.pack()

        #Login label
        self.l1 = Label(text="Username",bg="#f6f6f6", font=('Arial', 11))
        self.l1.place(x=30,y=270,height=30,width=100)
        #Login entry
        self.e1 = Entry(text="",bg='#EFEFEF',relief="flat")
        self.e1.place(x=45,y=300,height=50,width=255)

        #Password label
        self.l2 = Label(text="Password",bg="#f6f6f6", font=('Arial', 11))
        self.l2.place(x=30,y=390,height=30,width=100)
        #Password entry
        self.e2 = Entry(bg="#EFEFEF",relief="flat")
        self.e2.place(x=45,y=420,height=50,width=255)

        #Forgot_pwd Button
        self.f_pwd = Button(text="forgot password?",command=forgot_pwd,bd=0, fg="Black",underline=0 ,relief='flat', cursor="hand2",bg="#f6f6f6")
        self.f_pwd.place(x=200,y=475)

        #Submit Button
        self.submit = Button(text="Login",command=self.verify,bd=0,bg="#7028c6",fg="#FFFFFF",relief="flat",font=('Arial', 11))
        self.submit.place(x=45,y=530,height=45,width=150)
        
    #Verifying the entered info from the user.
    def verify(self):
        if self.e1.get()=="" or self.e2.get()=="":
            self.empty()
        elif self.e1.get()!= "Admin" or self.e2.get()!="123":
            self.error()
        elif self.e1.get()== "Admin" or self.e2.get()=="123":
            self.destroy()
        else:
            pass

    #If the entry box is empty 
    def empty(self):
        emp1=Label(text="Please Enter All the Details",fg="Black")
        emp1.place(x=42,y=230)
        emp1.config(bg="#f6f6f6",fg="#6177FE",font=('Arial',12))
        print(emp1)
        return    
    #If the entered info is incorrect
    def error(self):
        ero=Label(text="Username or Password is Incorrect")
        ero.place(x=42,y=230)
        ero.config(bg="#f6f6f6",fg="#6177FE",font=('Arial',12))
        print(ero)
        return

    #To destroy the above conditions
    def destroy(self):
        right=Label(text="                                                                                                            ")
        right.place(x=42,y=230)
        right.config(bg="#f6f6f6",fg="#6177FE",font=('Arial',12))
        print(right)
        return
        
    
        
window = Tk()
obj = Login(window)
window.state('zoomed')
window.mainloop()
