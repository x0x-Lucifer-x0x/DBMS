
from tkinter import *
from PIL import Image,ImageTk

from functions import absent


def attend():

     root = Tk()
     root.title("Attendance")
     root.geometry("1920x1080")
     root.config(bg="#f6f6f6")
    
     
     image = Image.open('media/attendance.png')
     image2 = image.resize((1530,  820), Image.ANTIALIAS)
     my_img = ImageTk.PhotoImage(image2)
     my_lbl = Label(image = my_img) 
     my_lbl.pack()


     heading = Label(text="Attendance",bg="#FFFFFF", font=('Lucida Console', 50))
     heading.place(x=40,y=40)
     
     def logout():
          absent(root)

     icon_image = Image.open('media/id_icon.png')
     icon_image = icon_image.resize((150,  150), Image.ANTIALIAS)
     my_img1 = ImageTk.PhotoImage(icon_image)

     mbtn = Menubutton(root,image=my_img1, text="",bg="#ffffff",bd=0, relief=RAISED)
     mbtn.place(x=1800,y=14,height="100",width="100")
     mbtn.menu = Menu(mbtn, tearoff = 0)
     mbtn["menu"] = mbtn.menu
        
     pythonVar = IntVar()
     javaVar = IntVar()
     phpVar = IntVar()

     mbtn.menu.add_checkbutton(label="Profile", variable=pythonVar)
     mbtn.menu.add_checkbutton(label="Help", variable=javaVar)
     mbtn.menu.add_checkbutton(label="Back",command=logout, variable=phpVar)

     l1 = Label(text="There is no Attendance uploaded for this month. Please try again later.",bg="#FFFFFF",fg="#5d53f1", font=('Lucida Console', 19))
     l1.place(x=210,y=710)   



     root.state('zoomed')
     root.mainloop()
