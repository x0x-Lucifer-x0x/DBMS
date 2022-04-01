from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from functions import stud
import mysql.connector
from tkinter import messagebox



def stu():
    root = Tk()
    root.title("Students")
    root.geometry("1920x1080")
    root.config(bg="#f6f6f6")

    #=====All Variables=====#
    roll_var = IntVar()
    name_var = StringVar()
    class_var = IntVar()
    div_var = StringVar()
    mail_var = StringVar()
    add_var = StringVar()
    Contact_var = IntVar()
    dob_var = StringVar()
    sex_var = StringVar()

    #Saves info to database
    def add_info():
        conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
        cursur=conn.cursor()
        cursur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                        roll_var.get(),name_var.get(),class_var.get(),
                                                        div_var.get(),mail_var.get(),add_var.get(),
                                                        Contact_var.get(),dob_var.get(),sex_var.get()
                                                        ))
        conn.commit()
        fetch()
        conn.close()
        
            

    #fetch data from database
    def fetch():
        conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
        cursur=conn.cursor()
        cursur.execute("select * from students")
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
        roll_var.set(data[0])
        name_var.set(data[1])
        class_var.set(data[2])
        div_var.set(data[3])
        mail_var.set(data[4])
        add_var.set(data[5])
        Contact_var.set(data[6])
        dob_var.set(data[7])
        sex_var.set(data[8])

    #delete info from database  
    def delete_info():
        delete=messagebox.askyesno("Delete","Are you sure to delete this student")
        if delete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
            cursur=conn.cursor()
            sql = "delete from students where rollno=%s"
            value=(roll_var.get(),)
            cursur.execute(sql,value)

        else:
            if not delete:
                return
        conn.commit()
        fetch()
        conn.close()
        messagebox.showinfo("Delete","Your data has been Deleted")

    #changes info in database
    def update_info():
        update=messagebox.askyesno("Update","Are sure to update this info")
        if update>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
            cursur=conn.cursor()
            sql = "delete from students where rollno=%s"
            value=(roll_var.get(),)
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
        roll_var.set("")
        name_var.set("")
        class_var.set("")
        div_var.set("")     
        mail_var.set("")
        add_var.set("")
        Contact_var.set("")
        dob_var.set("")
        sex_var.set("")

    #searches data by name,id,contact
    def search_info():
        conn=mysql.connector.connect(host="localhost",user="root",password="Meet@1234",database="stm")
        cursur=conn.cursor()
        cursur.execute("select * from students where "+str(search_var.get())+" LIKE '%"+str(e10_var.get())+"%'")
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
        stud(root)

    heading = Label(text="Students",bg="#FFFFFF", font=('Lucida Console', 50))
    heading.place(x=40,y=50)

    #dropbox
    icon_image = Image.open('media/id_icon.png')
    icon_image = icon_image.resize((150,  150), Image.ANTIALIAS)
    my_img1 = ImageTk.PhotoImage(icon_image)

    mbtn = Menubutton(root,image=my_img1, text="",bg="#ffffff",bd=0, relief=RAISED)
    mbtn.place(x=1400,y=18,height="100",width="100")
    mbtn.menu = Menu(mbtn, tearoff = 0)
    mbtn["menu"] = mbtn.menu
            
    pythonVar = IntVar()
    javaVar = IntVar()
    phpVar = IntVar()

    mbtn.menu.add_checkbutton(label="Profile", variable=pythonVar)
    mbtn.menu.add_checkbutton(label="Help", variable=javaVar)
    mbtn.menu.add_checkbutton(label="Back",command=logout, variable=phpVar)


    #entry details
    rollno = Label(text="Roll No.",bg="#FFFFFF", font=('Lucida Console', 14))
    rollno.place(x=30,y=220)
    e2 = Entry(textvariable=roll_var,bg='#EFEFEF',relief="flat")
    e2.place(x=145,y=223,height=25,width=230)

    name = Label(text="Name",bg="#FFFFFF", font=('Lucida Console', 17))
    name.place(x=30,y=280)
    e1 = Entry(textvariable=name_var,bg='#EFEFEF',relief="flat")
    e1.place(x=145,y=283,height=25,width=230)

    Class = Label(text="Class",bg="#FFFFFF", font=('Lucida Console', 14))
    Class.place(x=30,y=340)
    e3 = Entry(textvariable=class_var,bg='#EFEFEF',relief="flat")
    e3.place(x=105,y=340,height=25,width=65)

    div = Label(text="Section",bg="#FFFFFF", font=('Lucida Console', 14))
    div.place(x=210,y=340)
    e4 = Entry(textvariable=div_var,bg='#EFEFEF',relief="flat")
    e4.place(x=309,y=340,height=25,width=65)

    email = Label(text="Email",bg="#FFFFFF", font=('Lucida Console', 14))
    email.place(x=30,y=400)
    e5 = Entry(textvariable=mail_var,bg='#EFEFEF',relief="flat")
    e5.place(x=145,y=403,height=25,width=230)

    address = Label(text="Address",bg="#FFFFFF", font=('Lucida Console', 14))
    address.place(x=30,y=460)
    e6 = Entry(textvariable=add_var,bg='#EFEFEF',relief="flat")
    e6.place(x=145,y=463,height=45,width=230)

    contact = Label(text="Contact",bg="#FFFFFF", font=('Lucida Console', 14))
    contact.place(x=30,y=530)
    e7 = Entry(textvariable=Contact_var,bg='#EFEFEF',relief="flat")
    e7.place(x=145,y=533,height=25,width=230)

    dob = Label(text="D.O.B",bg="#FFFFFF", font=('Lucida Console', 14))
    dob.place(x=30,y=590)
    e8 = Entry(textvariable=dob_var,bg='#EFEFEF',relief="flat")
    e8.place(x=145,y=593,height=25,width=230)

    sex = Label(text="Gender",bg="#FFFFFF", font=('Lucida Console', 14))
    sex.place(x=30,y=650)
    e9 = Entry(textvariable=sex_var,bg='#EFEFEF',relief="flat")
    e9.place(x=145,y=653,height=25,width=230)


    #dml elements
    b = Button( root,text="Clear",bg="#EFEFEF",command=clear_info,fg="Black",relief="flat",font=('Lucida Console', 15))
    b.place(x=30,y=693,height=28,width=347)

    b1 = Button( root,text="Add",bg="#5d53f1",fg="#FFFFFF",command=add_info,relief="flat",font=('Lucida Console', 15))
    b1.place(x=30,y=740,height=30,width=80)

    b2 = Button( root,text="Update",bg="#5d53f1",command=update_info,fg="#FFFFFF",relief="flat",font=('Lucida Console', 14))
    b2.place(x=160,y=740,height=30,width=80)

    b3 = Button( root,text="Delete",bg="#5d53f1",command=delete_info,fg="#FFFFFF",relief="flat",font=('Lucida Console', 14))
    b3.place(x=285,y=740,height=30,width=80)


    #searching elements
    search = Label(text="Search By",bg="#FFFFFF", font=('Lucida Console', 14))
    search.place(x=470,y=230)

    search_var = StringVar()
    search_box = ttk.Combobox(font=('Lucida Console', 11),textvariable=search_var,state='readonly')
    search_box['values']=("Name","Rollno","Contact")
    search_box.place(x=590,y=230,height=25,width=95)

    e10_var = StringVar()
    e10= Entry(bg='#EFEFEF',textvariable=e10_var,relief="flat")
    e10.place(x=720,y=228,height=33,width=225)

    b4 = Button( root,text="Search",bg="#5d53f1",command=search_info,fg="#FFFFFF",relief="flat",font=('Lucida Console', 13))
    b4.place(x=1005,y=228,height=30,width=80)

    b5 = Button( root,text="Show All",bg="#5d53f1",command=fetch,fg="#FFFFFF",relief="flat",font=('Lucida Console', 13))
    b5.place(x=1122,y=228,height=30,width=95)

    frame = Frame(root,bd=1,bg="#f6f6f6")
    frame.place(x=470,y=290,height=450,width=753)


    scrollx = Scrollbar(frame,orient=HORIZONTAL)
    scrolly = Scrollbar(frame,orient=VERTICAL)
    table = ttk.Treeview(frame,columns=("roll","name","class","div",
                                        "Email","Add","Contact","dob","sex"),
                                        xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=table.xview)
    scrolly.config(command=table.yview)
    table.heading("roll",text="Roll no.")
    table.heading("name",text="Name")
    table.heading("class",text="Class")
    table.heading("div",text="Section")
    table.heading("Email",text="Email")
    table.heading("Add",text="Address")
    table.heading("Contact",text="Contact")
    table.heading("dob",text="D.O.B")
    table.heading("sex",text="Gender")
    table['show']='headings'
    table.column("roll",width=70)
    table.column("name",width=110)
    table.column("class",width=30)
    table.column("div",width=30)
    table.column("Email",width=110)
    table.column("Add",width=150)
    table.column("Contact",width=110)
    table.column("dob",width=70)
    table.column("sex",width=20)
    table.pack(fill=BOTH,expand=1)
    table.bind("<ButtonRelease-1>",get_cur)
    fetch()
    

    root.state('zoomed')
    root.mainloop()
