from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from functions import ivent
import mysql.connector
from tkinter import messagebox



def inventory():
    root = Tk()
    root.title("Inventory")
    root.geometry("1920x1080")
    root.config(bg="#f6f6f6")
                            
     #=====All Variables=====#
    id_var = IntVar()
    item_var = StringVar()
    name_var = StringVar()
    sup_var = StringVar()
    amt_var = IntVar()
    qty_var = IntVar()
    date_var = StringVar()

    #Saves info to database
    def add_info():
        conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
        cursur=conn.cursor()
        cursur.execute("insert into inventory values(%s,%s,%s,%s,%s,%s,%s)",(
                                                        id_var.get(),item_var.get(),
                                                        name_var.get(),sup_var.get(),
                                                        amt_var.get(),qty_var.get(),
                                                        date_var.get()
                                                        ))
        conn.commit()
        fetch()
        conn.close()
        
            

    #fetch data from database
    def fetch():
        conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
        cursur=conn.cursor()
        cursur.execute("select * from inventory")
        data=cursur.fetchall()
        if len(data)!=0:
            table.delete(*table.get_children())
            for i in data:
                table.insert("",END,values=i)
            conn.commit()
        conn.close()            

    #gets cursor 
    def get_cur(event=""):
        cursor_row=table.focus()
        content=table.item(cursor_row)
        data=content["values"]
        id_var.set(data[0])
        item_var.set(data[1])
        name_var.set(data[2])
        sup_var.set(data[3])
        amt_var.set(data[4])
        qty_var.set(data[5])
        date_var.set(data[6])
        

    #delete info from database  
    def delete_info():
        delete=messagebox.askyesno("Delete","Are you sure to delete this item")
        if delete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
            cursur=conn.cursor()
            sql = "delete from inventory where id=%s"
            value=(id_var.get(),)
            cursur.execute(sql,value)

        else:
            if not delete:
                return
        conn.commit()
        fetch()
        conn.close()
        

    #changes info in database
    def update_info():
        update=messagebox.askyesno("Update","Are you sure to update this info")
        if update>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
            cursur=conn.cursor()
            sql = "delete from inventory where id=%s"
            value=(id_var.get(),)
            cursur.execute(sql,value)

        else:
            if not update:
                return
        conn.commit()
        fetch()
        conn.close()
        add_info()

    #clears the entry 
    def clear_info():
        id_var.set("")
        item_var.set("")
        name_var.set("")
        sup_var.set("")
        amt_var.set("")
        qty_var.set("")
        date_var.set("")

    #searches data by name,id,contact
    def search_info():
        conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
        cursur=conn.cursor()
        cursur.execute("select * from inventory where "+str(search_var.get())+" LIKE '%"+str(e10_var.get())+"%'")
        data=cursur.fetchall()
        if len(data)!=0:
            table.delete(*table.get_children())
            for i in data:
                table.insert("",END,values=i)
            conn.commit()
        conn.close()

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

    #entry details
    id_lbl = Label(text="Item ID",bg="#FFFFFF", font=('Lucida Console', 14))
    id_lbl.place(x=30,y=355)
    e = Entry(bg='#EFEFEF',textvariable=id_var,relief="flat")
    e.place(x=145,y=355,height=25,width=230)

    item = Label(text="Item Name",bg="#FFFFFF", font=('Lucida Console', 14))
    item.place(x=30,y=412)
    e1 = Entry(bg='#EFEFEF',textvariable=item_var,relief="flat")
    e1.place(x=145,y=412,height=25,width=230)

    name = Label(text="Name",bg="#FFFFFF", font=('Lucida Console', 14))
    name.place(x=30,y=471)
    e2 = Entry(bg='#EFEFEF',textvariable=name_var,relief="flat")
    e2.place(x=145,y=471,height=25,width=230)

    sup = Label(text="Supplier",bg="#FFFFFF", font=('Lucida Console', 14))
    sup.place(x=30,y=531)
    e3 = Entry(bg='#EFEFEF',textvariable=sup_var,relief="flat")
    e3.place(x=150,y=531,height=25,width=225)

    amt = Label(text="Amount",bg="#FFFFFF", font=('Lucida Console', 14))
    amt.place(x=30,y=594)
    e5 = Entry(bg='#EFEFEF',textvariable=amt_var,relief="flat")
    e5.place(x=145,y=594,height=25,width=230)

    qty = Label(text="Quantity",bg="#FFFFFF", font=('Lucida Console', 14))
    qty.place(x=30,y=657)
    e6 = Entry(bg='#EFEFEF',textvariable=qty_var,relief="flat")
    e6.place(x=145,y=657,height=25,width=230)

    date = Label(text="Date",bg="#FFFFFF", font=('Lucida Console', 14))
    date.place(x=30,y=720)
    e7 = Entry(bg='#EFEFEF',textvariable=date_var,relief="flat")
    e7.place(x=145,y=720,height=25,width=230)


    b = Button( root,text="Clear",bg="#5d53f1",fg="#FFFFFF",relief="flat",command=clear_info,font=('Lucida Console', 15))
    b.place(x=1095,y=735,height=30,width=80)

    b1 = Button( root,text="Add",bg="#5d53f1",fg="#FFFFFF",command=add_info,relief="flat",font=('Lucida Console', 15))
    b1.place(x=570,y=735,height=30,width=80)

    b2 = Button( root,text="Update",bg="#5d53f1",fg="#FFFFFF",command=update_info,relief="flat",font=('Lucida Console', 15))
    b2.place(x=740,y=735,height=30,width=80)

    b3 = Button( root,text="Delete",bg="#5d53f1",fg="#FFFFFF",command=delete_info,relief="flat",font=('Lucida Console', 15))
    b3.place(x=920,y=735,height=30,width=80)

    #searching elements
    search = Label(text="Search :",bg="#FFFFFF", font=('Lucida Console', 19))
    search.place(x=30,y=240)

    search_var = StringVar()
    search_box = ttk.Combobox(font=('Lucida Console', 11),textvariable=search_var,state='readonly')
    search_box['values']=("ID","AMT","QTY")
    search_box.place(x=180,y=303,height=25,width=95)

    search_by = Label(text="Search By",bg="#FFFFFF", font=('Lucida Console', 16))
    search_by.place(x=30,y=303)

    e10_var = StringVar()
    e10= Entry(bg='#EFEFEF',textvariable=e10_var,relief="flat")
    e10.place(x=180,y=238,height=33,width=295)

    b4 = Button( root,text="Search",bg="#5d53f1",fg="#FFFFFF",command=search_info,relief="flat",font=('Lucida Console', 18))
    b4.place(x=345,y=303,height=30,width=110)

    frame = Frame(root,bd=1,bg="#f6f6f6")
    frame.place(x=535,y=220,height=450,width=703)


    scrollx = Scrollbar(frame,orient=HORIZONTAL)
    scrolly = Scrollbar(frame,orient=VERTICAL)
    table = ttk.Treeview(frame,columns=("id","item","name","sup","amount","quantity","date"),
                                        xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=table.xview)
    scrolly.config(command=table.yview)
    table.heading("id",text="ID")
    table.heading("item",text="Item Name")
    table.heading("name",text="Name")
    table.heading("sup",text="Supplier")
    table.heading("amount",text="Amount")
    table.heading("quantity",text="Quantity")
    table.heading("date",text="Date")
    table['show']='headings'
    table.column("id",width=40)
    table.column("item",width=110)
    table.column("name",width=110)
    table.column("sup",width=90)
    table.column("amount",width=100)
    table.column("quantity",width=60)
    table.column("date",width=80)
    table.pack(fill=BOTH,expand=1)
    table.bind("<ButtonRelease-1>",get_cur)
    fetch()



    root.state('zoomed')
    root.mainloop()

