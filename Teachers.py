from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk

from functions import empo

def teacher():
    root = Tk()
    root.title("Teachers")
    root.geometry("1920x1080")
    root.config(bg="#f6f6f6")


    #Bg img
    image = Image.open('Teacher.png')
    image = image.resize((1530,  820), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(image)
    my_lbl = Label(image = my_img) 
    my_lbl.pack()

    def logout():
        empo(root)

    heading = Label(text="Teachers",bg="#FFFFFF", font=('Lucida Console', 50))
    heading.place(x=40,y=50)

    #dropbox
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

    #entry details
    name = Label(text="Name",bg="#FFFFFF", font=('Lucida Console', 17))
    name.place(x=30,y=220)
    e1 = Entry(bg='#EFEFEF',relief="flat")
    e1.place(x=145,y=223,height=25,width=230)

    id = Label(text="ID",bg="#FFFFFF", font=('Lucida Console', 14))
    id.place(x=30,y=280)
    e2 = Entry(bg='#EFEFEF',relief="flat")
    e2.place(x=145,y=283,height=25,width=230)

    desig = Label(text="Designation",bg="#FFFFFF", font=('Lucida Console', 13))
    desig.place(x=30,y=340)
    e3 = Entry(bg='#EFEFEF',relief="flat")
    e3.place(x=150,y=340,height=25,width=225)

    email = Label(text="Email",bg="#FFFFFF", font=('Lucida Console', 14))
    email.place(x=30,y=400)
    e5 = Entry(bg='#EFEFEF',relief="flat")
    e5.place(x=145,y=403,height=25,width=230)

    add = Label(text="Address",bg="#FFFFFF", font=('Lucida Console', 14))
    add.place(x=30,y=460)
    e6 = Entry(bg='#EFEFEF',relief="flat")
    e6.place(x=145,y=463,height=45,width=230)

    phn = Label(text="Contact",bg="#FFFFFF", font=('Lucida Console', 14))
    phn.place(x=30,y=530)
    e7 = Entry(bg='#EFEFEF',relief="flat")
    e7.place(x=145,y=533,height=25,width=230)

    dob = Label(text="D.O.B",bg="#FFFFFF", font=('Lucida Console', 14))
    dob.place(x=30,y=590)
    e8 = Entry(bg='#EFEFEF',relief="flat")
    e8.place(x=145,y=593,height=25,width=230)

    sex = Label(text="Gender",bg="#FFFFFF", font=('Lucida Console', 14))
    sex.place(x=30,y=650)
    e9 = Entry(bg='#EFEFEF',relief="flat")
    e9.place(x=145,y=653,height=25,width=230)


    b = Button( root,text="Clear",bg="#EFEFEF",fg="Black",relief="flat",font=('Lucida Console', 15))
    b.place(x=30,y=693,height=28,width=347)

    b1 = Button( root,text="Add",bg="#5d53f1",fg="#FFFFFF",relief="flat",font=('Lucida Console', 15))
    b1.place(x=35,y=740,height=30,width=80)

    b2 = Button( root,text="Update",bg="#5d53f1",fg="#FFFFFF",relief="flat",font=('Lucida Console', 14))
    b2.place(x=160,y=740,height=30,width=80)

    b3 = Button( root,text="Delete",bg="#5d53f1",fg="#FFFFFF",relief="flat",font=('Lucida Console', 14))
    b3.place(x=285,y=740,height=30,width=80)

    #searching elements
    search = Label(text="Search By",bg="#FFFFFF", font=('Lucida Console', 14))
    search.place(x=470,y=230)

    search_box = ttk.Combobox(font=('Lucida Console', 11),state='readonly')
    search_box['values']=("Name","Roll no","Contact")
    search_box.place(x=590,y=230,height=25,width=95)

    e10= Entry(bg='#EFEFEF',relief="flat")
    e10.place(x=720,y=228,height=33,width=225)

    b4 = Button( root,text="Search",bg="#5d53f1",fg="#FFFFFF",relief="flat",font=('Lucida Console', 13))
    b4.place(x=1005,y=228,height=30,width=80)

    b5 = Button( root,text="Show All",bg="#5d53f1",fg="#FFFFFF",relief="flat",font=('Lucida Console', 13))
    b5.place(x=1122,y=228,height=30,width=95)

    frame = Frame(root,bd=1,bg="#f6f6f6")
    frame.place(x=470,y=290,height=450,width=753)


    scrollx = Scrollbar(frame,orient=HORIZONTAL)
    scrolly = Scrollbar(frame,orient=VERTICAL)
    table = ttk.Treeview(frame,columns=("id","name","desig","Email",
                                        "Add","phn","dob","sex"),
                                        xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=table.xview)
    scrolly.config(command=table.yview)
    table.heading("id",text="ID")
    table.heading("name",text="Name")
    table.heading("desig",text="Designation")
    table.heading("Email",text="Email")
    table.heading("Add",text="Address")
    table.heading("phn",text="Contact")
    table.heading("dob",text="D.O.B")
    table.heading("sex",text="Gender")
    table['show']='headings'
    table.column("id",width=70)
    table.column("name",width=110)
    table.column("desig",width=75)
    table.column("Email",width=110)
    table.column("Add",width=150)
    table.column("phn",width=110)
    table.column("dob",width=70)
    table.column("sex",width=20)
    table.pack(fill=BOTH,expand=1)



    root.state('zoomed')
    root.mainloop()

