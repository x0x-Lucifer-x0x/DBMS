from tkinter import * 
from PIL import Image,ImageTk




class Login:
    def __init__(self, window):
        window = window
        window.title("LOGIN PAGE")
        window.geometry("1920x1080")
        window.config(bg="#f6f6f6")
    

        #Bg img
        image = Image.open('hbg.jpg')
        image =  image.resize((1600,  850), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage( image)
        my_lbl = Label(image =  my_img) 
        my_lbl.pack()

        #Login label
        l1 = Label(text="Username",bg="#f6f6f6", font=('Arial', 13))
        l1.place(x=30,y=270,height=30,width=100)
        #Login entry
        e1 = Entry(text="",bg='#EFEFEF',relief="flat")
        e1.place(x=45,y=300,height=50,width=255)

        #Password label
        l2 = Label(text="Password",bg="#f6f6f6", font=('Arial', 13))
        l2.place(x=30,y=390,height=30,width=100)
        #Password entry
        e2 = Entry(bg="#EFEFEF",relief="flat")
        e2.place(x=45,y=420,height=50,width=255)

        #Forgot_pwd Button
        f_pwd = Button(text="forgot password?",command=f_pwd,bd=0, fg="Black",underline=0 ,relief='flat', cursor="hand2",bg="#f6f6f6")
        f_pwd.place(x=200,y=475)
        
        #Submit Button
        submit = Button(text="Login",command= verify,bd=0,bg="#7028c6",fg="#FFFFFF",relief="flat",font=('Arial', 11))
        submit.place(x=45,y=530,height=45,width=150)
        
    
        

    #Verifying the entered info from the user.
    def verify(self):
        if  e1.get()=="" or  e2.get()=="":
             empty()
        elif  e1.get()!= "Admin" or  e2.get()!="123":
             error()
        elif  e1.get()== "Admin" or  e2.get()=="123":
             destroy()
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

    
        
    '''def quit(self):
        quit = COMMAND=window.destroy() 
        return

    def open():
        call = COMMAND=forgot_pwd()
        return
    



        
         root = root
         root.title("Forgot Password")
         root.geometry("1920x1080")
         root.config(bg="#f6f6f6")

         image = Image.open('finalpwdbg.jpg')
         image =  image.resize((1600,  850), Image.ANTIALIAS)
         my_img = ImageTk.PhotoImage( image)
         my_lbl = Label(image =  my_img) 
         my_lbl.pack()
     
        

         b1 = Button( root,text="Back",bg="#f6f6f6",fg="Black",relief="flat",font=('Arial', 20))
         b1.place(x=1440,y=40,height=50,width=80)

         l1 = Label( root,text="Forgot Password",bg="#f6f6f6",fg="Black", font=('Arial', 30))
         l1.place(x=500,y=20,height=110,width=500)

         l2 = Label( root,text="Enter your Admission Number ",bg="#f6f6f6",fg="Black", font=('Arial', 11))
         l2.place(x=320,y=250,height="40",width="200")

         e1 = Entry( root,text="",bg='#EFEFEF',relief="flat")
         e1.place(x=320,y=290,height="100",width="850")

         b2 = Button( root,text="CONTINUE",bg="#7028c6",fg="#FFFFFF",relief="flat",font=('Arial', 11))
         b2.place(x=650,y=415,height="40",width="160")

        root = Tk()
         root.state('zoomed')
         root.mainloop()'''

def f_pwd():
    window.destroy()

    root = Tk()
    root.title("Forgot Password")
    root.geometry("1920x1080")
    root.config(bg="#f6f6f6")
    
    image = Image.open('finalfpwd1.jpg')
    image = image.resize((1600,  850), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(image)
    my_lbl = Label(image = my_img) 
    my_lbl.pack()
     

    b1 = Button( root,text="Back",bg="#f6f6f6",fg="Black",relief="flat",font=('Arial', 20))
    b1.place(x=1440,y=40,height=50,width=80)

    l1 = Label( root,text="Forgot Password",bg="#f6f6f6",fg="Black", font=('Arial', 30))
    l1.place(x=500,y=20,height=110,width=500)

    l2 = Label( root,text="Enter your Admission Number ",bg="#f6f6f6",fg="Black", font=('Arial', 11))
    l2.place(x=320,y=250,height="40",width="200")

    e1 = Entry( root,text="",bg='#EFEFEF',relief="flat")
    e1.place(x=320,y=290,height="100",width="850")

    b2 = Button( root,text="CONTINUE",bg="#7028c6",fg="#FFFFFF",relief="flat",font=('Arial', 11))
    b2.place(x=650,y=415,height="40",width="160")


    root.state('zoomed')
    root.mainloop()



window = Tk()
obj = Login(window)
window.state('zoomed')
window.mainloop()



