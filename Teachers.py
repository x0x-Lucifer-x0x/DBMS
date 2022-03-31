from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from functions import empo
import mysql.connector



def teacher():
    root = Tk()
    root.title("Teachers")
    root.geometry("1920x1080")
    root.config(bg="#f6f6f6")

    #variables
    id_var = IntVar()
    name_var = StringVar()
    desig_var = StringVar()
    mail_var = StringVar()
    add_var = StringVar()
    phn_var = IntVar()
    dob_var = StringVar()
    sex_var = StringVar()


    def add_info():
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
            cursur=conn.cursor()
            cursur.execute("insert into teachers values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                        id_var.get(),name_var.get(),desig_var.get(),
                                                        mail_var.get(),add_var.get(),phn_var.get(),
                                                        dob_var.get(),sex_var.get()
                                                        ))
            conn.commit()
            fetch()
            conn.close()
            #messagebox.showinfo("sucessfully added!",parent=root)
            

        except EXCEPTION as es:         
            conn.rollback()

    def fetch():
        conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
        cursur=conn.cursor()
        cursur.execute("select * from teachers")
        data=cursur.fetchall()
        if len(data)!=0:
            table.delete(*table.get_children())
            for i in data:
                table.insert("",END,values=i)
            conn.commit()
        conn.close()            


    def get_cur(event=""):
        cursor_row=table.focus()
        content=table.item(cursor_row)
        data=content["values"]
        id_var.set(data[0])
        name_var.set(data[1])
        desig_var.set(data[2])
        mail_var.set(data[3])
        add_var.set(data[4])
        phn_var.set(data[5])
        dob_var.set(data[6])
        sex_var.set(data[7])



    def delete_info():
        delete=messagebox.askyesno("Delete","Are sure delete this student")
        if delete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
            cursur=conn.cursor()
            sql = "delete from teachers where id=%s"
            value=(id_var.get(),)
            cursur.execute(sql,value)

        else:
            if not delete:
                return
        conn.commit()
        fetch()
        conn.close()
        messagebox.showinfo("Delete","Your data has been Deleted")

    def update_info():
        update=messagebox.askyesno("Update","Are sure to update this info")
        if update>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
            cursur=conn.cursor()
            sql = "delete from teachers where id=%s"
            value=(id_var.get(),)
            cursur.execute(sql,value)

        else:
            if not update:
                return
        conn.commit()
        fetch()
        conn.close()
        messagebox.showinfo("Update","Your data has been Updated")
        
        add_info()

    def clear_info():
        id_var.set("")
        name_var.set("")
        desig_var.set("")     
        mail_var.set("")
        add_var.set("")
        phn_var.set("")
        dob_var.set("")
        sex_var.set("")

    def search_info():
        conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
        cursur=conn.cursor()
        cursur.execute("select * from teachers where "+str(search_var.get())+" LIKE '%"+str(e10.get())+"%'")
        data=cursur.fetchall()
        if len(data)!=0:
            table.delete(*table.get_children())
            for i in data:
                table.insert("",END,values=i)
            conn.commit()
        conn.close()        


        

    #Bg img
    image = Image.open('media/Teacher.png')
    image = image.resize((1530,  820), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(image)
    my_lbl = Label(image = my_img) 
    my_lbl.pack()

    def logout():
        empo(root)

    heading = Label(text="Teachers",bg="#FFFFFF", font=('Lucida Console', 50))
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
    name = Label(text="Name",bg="#FFFFFF", font=('Lucida Console', 17))
    name.place(x=30,y=220)
    e1 = Entry(bg='#EFEFEF',textvariable=name_var,relief="flat")
    e1.place(x=145,y=223,height=25,width=230)

    id = Label(text="ID",bg="#FFFFFF", font=('Lucida Console', 14))
    id.place(x=30,y=280)
    e2 = Entry(bg='#EFEFEF',textvariable=id_var,relief="flat")
    e2.place(x=145,y=283,height=25,width=230)

    desig = Label(text="Designation",bg="#FFFFFF", font=('Lucida Console', 13))
    desig.place(x=30,y=340)
    e3 = Entry(bg='#EFEFEF',textvariable=desig_var,relief="flat")
    e3.place(x=150,y=340,height=25,width=225)

    email = Label(text="Email",bg="#FFFFFF", font=('Lucida Console', 14))
    email.place(x=30,y=400)
    e5 = Entry(bg='#EFEFEF',textvariable=mail_var,relief="flat")
    e5.place(x=145,y=403,height=25,width=230)

    add = Label(text="Address",bg="#FFFFFF", font=('Lucida Console', 14))
    add.place(x=30,y=460)
    e6 = Entry(bg='#EFEFEF',textvariable=add_var,relief="flat")
    e6.place(x=145,y=463,height=45,width=230)

    phn = Label(text="Contact",bg="#FFFFFF", font=('Lucida Console', 14))
    phn.place(x=30,y=530)
    e7 = Entry(bg='#EFEFEF',textvariable=phn_var,relief="flat")
    e7.place(x=145,y=533,height=25,width=230)

    dob = Label(text="D.O.B",bg="#FFFFFF", font=('Lucida Console', 14))
    dob.place(x=30,y=590)
    e8 = Entry(bg='#EFEFEF',textvariable=dob_var,relief="flat")
    e8.place(x=145,y=593,height=25,width=230)

    sex = Label(text="Gender",bg="#FFFFFF", font=('Lucida Console', 14))
    sex.place(x=30,y=650)
    e9 = Entry(bg='#EFEFEF',textvariable=sex_var,relief="flat")
    e9.place(x=145,y=653,height=25,width=230)


    b = Button( root,text="Clear",bg="#EFEFEF",fg="Black",command=clear_info,relief="flat",font=('Lucida Console', 15))
    b.place(x=30,y=693,height=28,width=347)

    b1 = Button( root,text="Add",bg="#5d53f1",command=add_info,fg="#FFFFFF",relief="flat",font=('Lucida Console', 15))
    b1.place(x=35,y=740,height=30,width=80)

    b2 = Button( root,text="Update",bg="#5d53f1",fg="#FFFFFF",command=update_info,relief="flat",font=('Lucida Console', 14))
    b2.place(x=160,y=740,height=30,width=80)

    b3 = Button( root,text="Delete",bg="#5d53f1",fg="#FFFFFF",command=delete_info,relief="flat",font=('Lucida Console', 14))
    b3.place(x=285,y=740,height=30,width=80)

    #searching elements
    search = Label(text="Search By",bg="#FFFFFF", font=('Lucida Console', 14))
    search.place(x=470,y=230)

    search_var=StringVar()
    search_box = ttk.Combobox(font=('Lucida Console', 11),textvariable=search_var,state='readonly')
    search_box['values']=("Name","ID","Contact")
    search_box.place(x=590,y=230,height=25,width=95)

    e10_var=StringVar()
    e10= Entry(bg='#EFEFEF',textvariable=e10_var,relief="flat")
    e10.place(x=720,y=228,height=33,width=225)

    b4 = Button( root,text="Search",bg="#5d53f1",fg="#FFFFFF",command=search_info,relief="flat",font=('Lucida Console', 13))
    b4.place(x=1005,y=228,height=30,width=80)

    b5 = Button( root,text="Show All",command=fetch,bg="#5d53f1",fg="#FFFFFF",relief="flat",font=('Lucida Console', 13))
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
    table.bind("<ButtonRelease>",get_cur)
    fetch()
    

    root.state('zoomed')
    root.mainloop()

teacher()
