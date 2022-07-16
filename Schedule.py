
from tkinter import *
from PIL import Image,ImageTk
from functions import dule

def Sched():

     root = Tk()
     root.title("Schedule")
     root.geometry("1920x1080")
     root.config(bg="#f6f6f6")
    
    
     image = Image.open('media/schedule.png')
     image2 = image.resize((1000,  700), Image.ANTIALIAS)
     my_img = ImageTk.PhotoImage(image2)
     my_lbl = Label(image = my_img) 
     my_lbl.pack()

          
     def logout():
          dule(root)

     icon_image = Image.open('media/id_icon.png')
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


  