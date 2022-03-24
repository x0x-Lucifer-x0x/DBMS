
import tkinter
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from functions import fis


def fee():

     root = Tk()
     root.title("Fee Structure")
     root.geometry("1920x1080")
     root.config(bg="#f6f6f6")
    
    
     image = Image.open('Fee_Structure.png')
     image = image.resize((1000,  700), Image.ANTIALIAS)
     my_img = ImageTk.PhotoImage(image)
     my_lbl = Label(image = my_img) 
     my_lbl.pack()

     def logout():
         fis(root)

     icon_image = Image.open('id_icon.png')
     icon_image = icon_image.resize((100,  100), Image.ANTIALIAS)
     my_img1 = ImageTk.PhotoImage(icon_image)

  
     mbtn = Menubutton(root,image=my_img1, text="",bg="#ffffff",bd=0, relief=RAISED)
     mbtn.place(x=900,y=2,height="100",width="100")
     mbtn.menu = Menu(mbtn, tearoff = 0)
     mbtn["menu"] = mbtn.menu
        
     pythonVar = IntVar()
     javaVar = IntVar()
     phpVar = IntVar()

     mbtn.menu.add_checkbutton(label="Profile", variable=pythonVar)
     mbtn.menu.add_checkbutton(label="Help", variable=javaVar)
     mbtn.menu.add_checkbutton(label="Back",command=logout, variable=phpVar)

    

     root.state('zoomed')
     root.mainloop()



