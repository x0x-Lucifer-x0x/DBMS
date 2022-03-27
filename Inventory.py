from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from functions import ivent
 
    #jfdyjfikgukgukgvkugmkkgukgkugkugkg,uug,jhyvfvjvfhyjvghyjvgyjgv

def inventory():
    root = Tk()
    root.title("Inventory")
    root.geometry("1920x1080")
    root.config(bg="#f6f6f6")


    #Bg img
    image = Image.open('media/iventory.png')
    image = image.resize((1530,  820), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(image)
    my_lbl = Label(image = my_img) 
    my_lbl.pack()

    def logout():
        ivent(root)


    heading = Label(text="Inventory",bg="#FFFFFF", font=('Lucida Console', 50))
    heading.place(x=40,y=50)

    #dropbox
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

    #entry details
    item = Label(text="Item Name",bg="#FFFFFF", font=('Lucida Console', 14))
    item.place(x=30,y=388)
    e1 = Entry(bg='#EFEFEF',relief="flat")
    e1.place(x=145,y=388,height=25,width=230)

    name = Label(text="Name",bg="#FFFFFF", font=('Lucida Console', 14))
    name.place(x=30,y=451)
    e2 = Entry(bg='#EFEFEF',relief="flat")
    e2.place(x=145,y=451,height=25,width=230)

    sup = Label(text="Supplier",bg="#FFFFFF", font=('Lucida Console', 14))
    sup.place(x=30,y=511)
    e3 = Entry(bg='#EFEFEF',relief="flat")
    e3.place(x=150,y=511,height=25,width=225)

    amt = Label(text="Amount",bg="#FFFFFF", font=('Lucida Console', 14))
    amt.place(x=30,y=574)
    e5 = Entry(bg='#EFEFEF',relief="flat")
    e5.place(x=145,y=574,height=25,width=230)

    qty = Label(text="Quantity",bg="#FFFFFF", font=('Lucida Console', 14))
    qty.place(x=30,y=637)
    e6 = Entry(bg='#EFEFEF',relief="flat")
    e6.place(x=145,y=637,height=25,width=230)

    date = Label(text="Date",bg="#FFFFFF", font=('Lucida Console', 14))
    date.place(x=30,y=700)
    e7 = Entry(bg='#EFEFEF',relief="flat")
    e7.place(x=145,y=700,height=25,width=230)


    b = Button( root,text="Clear",bg="#5d53f1",fg="#FFFFFF",relief="flat",font=('Lucida Console', 15))
    b.place(x=1095,y=735,height=30,width=80)

    b1 = Button( root,text="Add",bg="#5d53f1",fg="#FFFFFF",relief="flat",font=('Lucida Console', 15))
    b1.place(x=570,y=735,height=30,width=80)

    b2 = Button( root,text="Update",bg="#5d53f1",fg="#FFFFFF",relief="flat",font=('Lucida Console', 15))
    b2.place(x=740,y=735,height=30,width=80)

    b3 = Button( root,text="Delete",bg="#5d53f1",fg="#FFFFFF",relief="flat",font=('Lucida Console', 15))
    b3.place(x=920,y=735,height=30,width=80)

    #searching elements
    search = Label(text="Search By",bg="#FFFFFF", font=('Lucida Console', 17))
    search.place(x=30,y=240)

    e10= Entry(bg='#EFEFEF',relief="flat")
    e10.place(x=180,y=238,height=33,width=295)

    b4 = Button( root,text="Search",bg="#5d53f1",fg="#FFFFFF",relief="flat",font=('Lucida Console', 18))
    b4.place(x=345,y=303,height=30,width=110)

    frame = Frame(root,bd=1,bg="#f6f6f6")
    frame.place(x=535,y=220,height=450,width=703)


    scrollx = Scrollbar(frame,orient=HORIZONTAL)
    scrolly = Scrollbar(frame,orient=VERTICAL)
    table = ttk.Treeview(frame,columns=("item","name","sup","amt","qty","date"),
                                        xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=table.xview)
    scrolly.config(command=table.yview)
    table.heading("item",text="Item Name")
    table.heading("name",text="Name")
    table.heading("sup",text="Supplier")
    table.heading("amt",text="Amount")
    table.heading("qty",text="Quantity")
    table.heading("date",text="Date")
    table['show']='headings'
    table.column("item",width=110)
    table.column("name",width=110)
    table.column("sup",width=90)
    table.column("amt",width=100)
    table.column("qty",width=60)
    table.column("date",width=80)
    table.pack(fill=BOTH,expand=1)



    root.state('zoomed')
    root.mainloop()


