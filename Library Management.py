from tkinter import *
import sqlite3
import sqlite3
from PIL import Image,ImageTk
class main_frame:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=900, width=900)
        self.f.propagate(0)
        self.f.pack()
        self.photo_ = Image.open("newww.jpg")  
        self.photo_copy = self.photo_.copy()
        self.image_ = ImageTk.PhotoImage(self.photo_)
        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)
        self.db = sqlite3.connect('try5')
        self.cursor = self.db.cursor()

       
        self.button1 = Button(self.f, text = 'Student', width = 40,activebackground = "coral", command = self.student,font='Courier 10')
        self.button2 = Button(self.f, text = 'Librarian', width = 40, command = self.lib,font='Courier 10',activebackground = "coral")
        self.button3 = Button(self.f, text = 'EXIT', width = 40, command = self.close_windows,font='Courier 10',activebackground = "coral")

        self.button4 = Button(self.f, text = 'Create', width = 40, command = self.create_table,font='Courier 10',activebackground = "coral")
        self.button5 = Button(self.f, text = 'Insert', width = 40, command = self.insert_table,font='Courier 10',activebackground = "coral")
        
        self.button1.place(x=300,y=200)
        self.button2.place(x=300,y=300)
        self.button3.place(x=300,y=400)

        self.master.resizable(height=False,width=False)
        #self.button4.place(x=300,y=500)
        #self.button5.place(x=300,y=600)

    def student(self):
        self.newWindow = Toplevel(self.master)
        self.app = student_login(self.newWindow)

    def lib(self):
        self.newWindow = Toplevel(self.master)
        self.app = lib_login(self.newWindow)
        
    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)

    def close_windows(self):
        self.master.destroy()

#create
    def create_table(self):
        self.createstr = "create table lib (l_id int primary key,l_name text )"
        self.cursor.execute(self.createstr)
        self.db.commit()

    def insert_table(self):
        self.insertsql = "insert into lib (l_id ,l_name ) values (103,'anirudh')"
        self.cursor.execute(self.insertsql)
        self.db.commit() 

#student login

class student_login:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=600,width=900)
        self.f.propagate(0)
        self.f.pack()

        self.db = sqlite3.connect('try5')
        self.cursor = self.db.cursor()
        self.photo_ = Image.open("student.jpg")  
        self.photo_copy = self.photo_.copy()
        self.image_ = ImageTk.PhotoImage(self.photo_)
        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)

        self.e1=Entry(self.f,width=12,fg="black",bg="ghost white",font=('Courier',10))
        self.e2=Entry(self.f,width=12,fg="black",bg="ghost white",font=('Courier',10))

        self.l1 = Label(self.master,text="Student login id",font='Courier 10')
        self.l2 = Label(self.master,text="Student Name ",font='Courier 10')

        
        self.button1 = Button(self.f, text = 'Login', width = 35, command = self.new_window1,font='Courier 10',activebackground = "Sky Blue1")
        self.button2 = Button(self.f, text = 'Back', width = 35, command = self.close_windows,font='Courier 10',activebackground = "Sky Blue1")
        
        self.l1.place(x=180,y=250)
        self.l2.place(x=180,y=300)
        self.e1.place(x=350,y=250)
        self.e2.place(x=350,y=300)
        self.button1.place(x=200 ,y=400)
        self.button2.place(x=200,y=500)
        self.master.resizable(height=False,width=False)
     
    def new_window1(self):
        self.check1=self.e1.get()
        self.check2=self.e2.get()

        if self.check1=='' or self.check2=='':
            self.newWindow = Toplevel(self.master)
            self.app = enter_values(self.newWindow)
        else:
            self.cursor.execute("select student_name from student1 where s_id='{}' ".format(self.e1.get()))
            self.r=self.cursor.fetchall()
            if not self.r:
                self.newWindow = Toplevel(self.master)
                self.app = incorrect_id(self.newWindow)
            else:
                self.newWindow = Toplevel(self.master)
                self.app = student_frame(self.newWindow)

        self.e1.delete(0,END)
        self.e2.delete(0,END)
            
    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)
        
    def close_windows(self):
        self.master.destroy()

#librarian login

class lib_login:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=600,width=900)
        self.f.propagate(0)
        self.f.pack()

        self.db = sqlite3.connect('try5')
        self.cursor = self.db.cursor()
        self.photo_ = Image.open("frame.jpg")  
        self.photo_copy = self.photo_.copy()
        self.image_ = ImageTk.PhotoImage(self.photo_)
        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)

        self.e1=Entry(self.f,width=12,fg="black",bg="ghost white",font=('Courier',10))
        self.e2=Entry(self.f,width=12,fg="black",bg="ghost white",font=('Courier',10))

        self.l1 = Label(self.master,text="Librarian login id",font='Courier 10')
        self.l2 = Label(self.master,text="Librarian Name",font='Courier 10')

        
        self.button1 = Button(self.f, text = 'Login', width = 35, command = self.new_window2,font='Courier 10',activebackground = "light goldenrod")
        self.button2 = Button(self.f, text = 'Back', width = 35, command = self.close_windows,font='Courier 10',activebackground = "light goldenrod")
        
        self.l1.place(x=180,y=250)
        self.l2.place(x=180,y=300)
        self.e1.place(x=350,y=250)
        self.e2.place(x=350,y=300)
        self.button1.place(x=200,y=400)
        self.button2.place(x=200,y=500)

        self.master.resizable(height=False,width=False)

    def new_window2(self):
        self.check1=self.e1.get()
        self.check2=self.e2.get()

        if self.check1=='' or self.check2=='':
            self.newWindow = Toplevel(self.master)
            self.app = enter_values(self.newWindow)
        else:
            self.cursor.execute("select * from lib where l_id='{}' ".format(self.e1.get()))
            self.r=self.cursor.fetchall()
            if not self.r:
                self.newWindow = Toplevel(self.master)
                self.app = incorrect_id(self.newWindow)
            else:
                self.newWindow = Toplevel(self.master)
                self.app = librarian_frame(self.newWindow)

        self.e1.delete(0,END)
        self.e2.delete(0,END)
                
    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)

    def close_windows(self):
        self.master.destroy()
        
#student and librarian window

        
class student_frame:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=600,width=900)
        self.f.propagate(0)
        self.f.pack()
        self.photo_ = Image.open("view1.jpg")  
        self.photo_copy = self.photo_.copy()
        self.image_ = ImageTk.PhotoImage(self.photo_)
        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)
        self.button1 = Button(self.f, text = 'View', width = 25, command = self.record_windowB,font='Courier 10',activebackground = "pale green")
        self.button2 = Button(self.f, text = 'Issue', width = 25, command = self.issue_window,font='Courier 10',activebackground = "pale green")
        self.button3 = Button(self.f, text = 'Back', width = 25, command = self.close_windows,font='Courier 10',activebackground = "pale green")
        
        self.button1.place(x=300,y=250)
        self.button2.place(x=300,y=300)
        self.button3.place(x=300,y=350)
        self.master.resizable(height=False,width=False)


    def issue_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = issue_frame(self.newWindow)

    def record_windowB(self):
        self.newWindow = Toplevel(self.master)
        self.app = record_frameB(self.newWindow)
        
    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))
        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)
    def close_windows(self):
        self.master.destroy()


class librarian_frame:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=600,width=900)
        self.f.propagate(0)
        self.f.pack()

        self.db = sqlite3.connect('try5')
        self.cursor = self.db.cursor()
        self.photo_ = Image.open("libc.jpg")  
        self.photo_copy = self.photo_.copy()
        self.image_ = ImageTk.PhotoImage(self.photo_)
        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)
        self.button1 = Button(self.f, text = 'Create Table', width = 25, command = self.createtableB,font='Courier 10',activebackground = "orchid1")
        self.button2 = Button(self.f, text = 'Add Books', width = 25, command = self.add_windowB,font='Courier 10',activebackground = "orchid1")
        self.button3 = Button(self.f, text = 'View Books', width = 25, command = self.record_windowB,font='Courier 10',activebackground = "orchid1")
        self.button4 = Button(self.f, text = 'Create Table', width = 25, command = self.createtableS,font='Courier 10',activebackground = "orchid1")
        self.button5 = Button(self.f, text = 'Add Students', width = 25, command = self.add_windowS,font='Courier 10',activebackground = "orchid1")
        self.button6 = Button(self.f, text = 'View Students', width = 25, command = self.record_windowS,font='Courier 10',activebackground = "orchid1")
        self.button7 = Button(self.f, text = 'Back', width = 25, command = self.close_windows,font='Courier 10',activebackground = "orchid1")
        self.button1.place(x=300,y=100)
        self.button2.place(x=300,y=130)
        self.button3.place(x=300,y=160)
        self.button4.place(x=300,y=190)
        self.button5.place(x=300,y=220)
        self.button6.place(x=300,y=250)
        self.button7.place(x=300,y=280)

        self.master.resizable(height=False,width=False)
        
    def close_windows(self):
        self.master.destroy()
        
    def add_windowB(self):
        self.newWindow = Toplevel(self.master)
        self.app = add_frameB(self.newWindow)

    def add_windowS(self):
        self.newWindow = Toplevel(self.master)
        self.app = add_frameS(self.newWindow)

    def record_windowB(self):
        self.newWindow = Toplevel(self.master)
        self.app = record_frameB(self.newWindow)

    def record_windowS(self):
        self.newWindow = Toplevel(self.master)
        self.app = record_frameS(self.newWindow)
        
    def createtableB(self):
        self.createstr = "create table books1 (book_id int primary key,book_name text ,author1 text ,author2 text ,publisher text ,noc int,type text)"
        self.cursor.execute(self.createstr)
        self.db.commit()

    def createtableS(self):
        self.createstr = "create table student1 (s_id int primary key,student_name text ,roll_no int,div text ,branch text ,year text)"
        self.cursor.execute(self.createstr)
        self.db.commit()

    '''def printrecord(self):
        self.cursor.execute("select * from books1")
        for r in self.cursor.fetchall():
            print("books name : {} {}".format(r[0],r[1]) )'''
    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)
    
#student options

#issue books
class issue_frame:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=600,width=900)
        self.f.propagate(0)
        self.f.pack()
        self.count=1
        self.db = sqlite3.connect('try5')
        self.cursor = self.db.cursor()
        self.photo_ = Image.open("book3.jpg")  
        self.photo_copy = self.photo_.copy()
        self.image_ = ImageTk.PhotoImage(self.photo_)
        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)
        self.button1 = Button(self.f, text = 'Confirm', width = 25,command = self.confirm_windows,font='Courier 10')
        self.button2 = Button(self.f, text = 'Back', width = 25, command = self.close_windows,font='Courier 10')
        
        

        self.button1 = Button(self.f, text = 'Confirm', width = 25,command = self.confirm_windows,font='Courier 10',activebackground = "lime green")
        self.button2 = Button(self.f, text = 'Back', width = 25, command = self.close_windows,font='Courier 10',activebackground = "lime green")
        
        self.l1 = Label(self.master,text="Book Name",font='Helvetica')
        self.l2 = Label(self.master,text="Book id",font='Helvetica')

        self.e1=Entry(self.f,width=18,fg="black",bg="ghost white",font=('Courier',10))
        self.e2=Entry(self.f,width=18,fg="black",bg="ghost white",font=('Courier',10))

        self.button1.place(x=300,y=230)
        self.button2.place(x=300,y=280)
        self.l1.place(x=130,y=150)
        self.l2.place(x=130,y=190)
        self.e1.place(x=250,y=150)
        self.e2.place(x=250,y=190)

        self.master.resizable(height=False,width=False)
            
    def confirm_windows(self):
        self.b_id=self.e2.get()
        self.check1=self.e1.get()

        if self.check1=='' or self.b_id=='':
            self.newWindow = Toplevel(self.master)
            self.app = enter_values(self.newWindow)
        else:
            self.cursor.execute("select * from books1 where book_id='{}' ".format(self.e2.get()))
            self.r=self.cursor.fetchall()
            if not self.r:
                self.newWindow = Toplevel(self.master)
                self.app = incorrect_id(self.newWindow)
            else:
                self.cursor.execute("select * from books1 where book_id like '{}'".format(self.b_id))
                for r in self.cursor.fetchall():
                    self.count=r[5]
                
                
                if self.count==0:
                    self.newWindow = Toplevel(self.master)
                    self.app = unconfirm_frame(self.newWindow)
                else:   
                    self.count=self.count-1
                    self.db.commit()
                    print(self.count)
                    self.cursor.execute("update books1 set noc = '{}' where book_id like '{}' ".format(self.count,self.b_id))  
                    self.db.commit()

                    self.newWindow = Toplevel(self.master)
                    self.app = confirm_frame(self.newWindow)

        self.e1.delete(0,END)
        self.e2.delete(0,END)
        
    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)
            
    def close_windows(self):
        self.master.destroy()
        
#confirm frame
class confirm_frame:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=200,width=400)
        self.f.propagate(0)
        self.f.pack()
        
        self.l4 = Label(self.master,text="Your Book is Issued", font='Helvetica')

        self.l4.place(x=25,y=50)
        self.button1 = Button(self.f, text = 'OK', width = 25, command = self.close_windows,font='Courier 10',activebackground = "pale green")
        self.button1.place(x=50,y=100)
        self.master.resizable(height=False,width=False)
                      
    def close_windows(self):
        self.master.destroy()

        
#librarian options
class add_frameB:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=600,width=900)
        self.f.propagate(0)
        self.f.pack()

        self.db = sqlite3.connect('try5')
        self.cursor = self.db.cursor()
        self.photo_ = Image.open("book2.jpg")  
        self.photo_copy = self.photo_.copy()
        self.image_ = ImageTk.PhotoImage(self.photo_)
        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)

        self.e1=Entry(self.f,width=18,fg="black",bg="ghost white",font=('Courier',10))
        self.e2=Entry(self.f,width=18,fg="black",bg="ghost white",font=('Courier',10))
        self.e3=Entry(self.f,width=18,fg="black",bg="ghost white",font=('Courier',10))
        self.e4=Entry(self.f,width=18,fg="black",bg="ghost white",font=('arial',12))
        self.e5=Entry(self.f,width=18,fg="black",bg="ghost white",font=('arial',12))
        self.e6=Entry(self.f,width=18,fg="black",bg="ghost white",font=('arial',12))
        self.e7=Entry(self.f,width=18,fg="black",bg="ghost white",font=('arial',12))
        self.l1=Label(self.master,text="Book Id",font='Helvetica')
        self.l2=Label(self.master,text="Book Name",font='Helvetica')
        self.l3=Label(self.master,text="Book author1",font='Helvetica')
        self.l4=Label(self.master,text="Book author2",font='Helvetica')
        self.l5=Label(self.master,text="Publisher",font='Helvetica')
        self.l6=Label(self.master,text="No of copies",font='Helvetica')
        self.l7=Label(self.master,text="Book Type",font='Helvetica')
        self.button1 = Button(self.f, text = 'Back', width = 25, command = self.close_windows,font='Courier 10',activebackground = "olive drab")
        self.button2 = Button(self.f, text = 'Add', width = 25, command = self.insertrecord,font='Courier 10',activebackground = "olive drab")
      
        self.button1.place(x=300,y=400)
        self.button2.place(x=300,y=280)
        self.e1.place(x=200,y=30)
        self.e2.place(x=200,y=60)
        self.e3.place(x=200,y=90)
        self.e4.place(x=200,y=120)
        self.e5.place(x=200,y=150)
        self.e6.place(x=200,y=180)
        self.e7.place(x=200,y=210)
        self.l1.place(x=60,y=30)
        self.l2.place(x=60,y=60)
        self.l3.place(x=60,y=90)
        self.l4.place(x=60,y=120)
        self.l5.place(x=60,y=150)
        self.l6.place(x=60,y=180)
        self.l7.place(x=60,y=210)
        self.master.resizable(height=False,width=False)
        

    def insertrecord(self):
        #self.id=int(self.e1.get())
        self.name=self.e2.get()
        self.author1=self.e3.get()
        self.author2=self.e4.get()
        self.pub=self.e5.get()
        self.type=self.e7.get()
        #self.noc=int(self.e6.get())

        self.check1=self.e1.get()
        self.check2=self.e6.get()
        if self.check1=='' or self.name=='' or self.author1=='' or self.pub=='' or self.check2=='' or self.type=='':
            self.newWindow = Toplevel(self.master)
            self.app = enter_values(self.newWindow)
        else:
            self.id=int(self.e1.get())
            self.noc=int(self.e6.get())
            
            self.cursor.execute("select * from books1 where book_id='{}' ".format(self.e1.get()))
            self.r=self.cursor.fetchall()
            if self.r:
                self.newWindow = Toplevel(self.master)
                self.app = incorrect_id(self.newWindow)
            else:
                self.insertsql = "insert into books1 (book_id ,book_name ,author1 ,author2 ,publisher ,noc ,type) values ('%d','%s','%s','%s','%s','%d','%s')"%(self.id,self.name,self.author1,self.author2,self.pub,self.noc,self.type)
                self.cursor.execute(self.insertsql)
                self.db.commit()
                self.newWindow = Toplevel(self.master)
                self.app = value_added(self.newWindow)

        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)
        self.e6.delete(0,END)
        self.e7.delete(0,END)
        
    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)
        
    def close_windows(self):
        self.master.destroy()

class record_frameB:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=900,width=1500)
        self.f.propagate(0)
        self.f.pack()

        self.db = sqlite3.connect('try5')
        self.cursor = self.db.cursor()
        
        #self.master.resizable(height=False,width=False)
        
        self.button1 = Button(self.f, text = 'Print', width = 15, command = self.print_onscreen,font='Courier 10',activebackground = "deep pink")
        self.button2 = Button(self.f, text = 'Back', width = 15, command = self.close_windows,font='Courier 10',activebackground = "deep pink")
        
        self.button1.place(x=35,y=500)
        self.button2.place(x=35,y=600)

        self.s1 = Spinbox(self.master,values=('fiction','technical'))
        self.s1.place(x=35,y=400)

    def close_windows(self):
        self.master.destroy()

    def print_onscreen(self):
        self.value = self.s1.get()
        print(self.value)
        self.cursor.execute("select * from books1 where type = '{}' ".format(self.value))
        r=self.cursor.fetchall()
        self.l2=Label(self.master,text="Book Id",width=15,font=('Helvetica'))
        self.l2.place(x=175,y=20)
        self.l3=Label(self.master,text="Book Name",width=15,font=('Helvetica'))
        self.l3.place(x=175*2,y=20)
        self.l4=Label(self.master,text="Author 1",width=15,font=('Helvetica'))
        self.l4.place(x=175*3,y=20)
        self.l5=Label(self.master,text="Author 2",width=15,font=('Helvetica'))
        self.l5.place(x=175*4,y=20)
        self.l6=Label(self.master,text="Publisher",width=15,font=('Helvetica'))
        self.l6.place(x=175*5,y=20)
        self.l7=Label(self.master,text="No.of copies",width=15,font=('Helvetica'))
        self.l7.place(x=175*6,y=20)
        self.l8=Label(self.master,text="Book Type",width=15,font=('Helvetica'))
        self.l8.place(x=175*7,y=20)

        for a in range(1,10):
            for b in range(1,10):
                self.l5=Label(self.master,text="\t\t\t\t\t\t",width=400,height=200)
                self.l5.place(x=175*a,y=50*b)
        for a in range(0,len(r)):
            for b in range(0,7):
                self.l1=Label(self.master,text=r[a][b],width=15,font=('Helvetica'))
                self.l1.place(x=175*(b+1),y=50*(a+1))

class add_frameS:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=900,width=900)
        self.f.propagate(0)
        self.f.pack()

        self.db = sqlite3.connect('try5')
        self.cursor = self.db.cursor()
        self.photo_ = Image.open("addd.jpg")  
        self.photo_copy = self.photo_.copy()
        self.image_ = ImageTk.PhotoImage(self.photo_)
        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)

        self.e1=Entry(self.f,width=18,fg="black",bg="ghost white",font=('arial',12))
        self.e2=Entry(self.f,width=18,fg="black",bg="ghost white",font=('arial',12))
        self.e3=Entry(self.f,width=18,fg="black",bg="ghost white",font=('arial',12))
        self.e4=Entry(self.f,width=18,fg="black",bg="ghost white",font=('arial',12))
        self.e5=Entry(self.f,width=18,fg="black",bg="ghost white",font=('arial',12))
        self.e6=Entry(self.f,width=18,fg="black",bg="ghost white",font=('arial',12))
        self.l1=Label(self.master,text="Student ID",font='Helvetica')
        self.l2=Label(self.master,text="Student Name",font='Helvetica')
        self.l3=Label(self.master,text="Roll No",font='Helvetica')
        self.l4=Label(self.master,text="Division",font='Helvetica')
        self.l5=Label(self.master,text="Branch",font='Helvetica')
        self.l6=Label(self.master,text="Year",font='Helvetica')
        self.button1 = Button(self.f, text = 'Back', width = 25, command = self.close_windows,font='Courier 10',activebackground = "light cyan")
        self.button2 = Button(self.f, text = 'Add', width = 25, command = self.insertrecord,font='Courier 10',activebackground = "light cyan")
      
        self.button1.place(x=300,y=400)
        self.button2.place(x=300,y=280)
        self.e1.place(x=200,y=30)
        self.e2.place(x=200,y=60)
        self.e3.place(x=200,y=90)
        self.e4.place(x=200,y=120)
        self.e5.place(x=200,y=150)
        self.e6.place(x=200,y=180)
        self.l1.place(x=60,y=30)
        self.l2.place(x=60,y=60)
        self.l3.place(x=60,y=90)
        self.l4.place(x=60,y=120)
        self.l5.place(x=60,y=150)
        self.l6.place(x=60,y=180)
        self.master.resizable(height=False,width=False)
        
    def insertrecord(self):
        #self.id=int(self.e1.get())
        self.name =self.e2.get()
        #self.rno=int(self.e3.get())
        self.div=self.e4.get()
        self.branch=self.e5.get()
        self.year=self.e6.get()

        self.check1=self.e1.get()
        self.check3=self.e3.get()
        if self.check1=='' or self.name=='' or self.check3=='' or self.div=='' or self.branch=='' or self.year=='':
            self.newWindow = Toplevel(self.master)
            self.app = enter_values(self.newWindow)
        else:
            self.id=int(self.e1.get())
            self.rno=int(self.e3.get())
            self.cursor.execute("select * from student1 where s_id='{}' ".format(self.e1.get()))
            self.r=self.cursor.fetchall()
            if self.r:
                self.newWindow = Toplevel(self.master)
                self.app = incorrect_id(self.newWindow)
            else:
                self.insertsql = "insert into student1 (s_id ,student_name ,roll_no ,div ,branch ,year) values ('%d','%s','%d','%s','%s','%s')"%(self.id,self.name,self.rno,self.div,self.branch,self.year)
                self.cursor.execute(self.insertsql)
                self.db.commit()
                self.newWindow = Toplevel(self.master)
                self.app = value_added(self.newWindow)

        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)
        self.e6.delete(0,END)
            
    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)
        
    def close_windows(self):
        self.master.destroy()

class record_frameS:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=900,width=1500)
        self.f.propagate(0)
        self.f.pack()

        self.db = sqlite3.connect('try5')
        self.cursor = self.db.cursor()
        
        self.button1 = Button(self.f, text = 'Print', width = 25, command = self.print_onscreen,font='Courier 10',activebackground = "olive drab")
        self.button2 = Button(self.f, text = 'Back', width = 25, command = self.close_windows,font='Courier 10',activebackground = "olive drab")
        
        self.button1.place(x=35,y=500)
        self.button2.place(x=35,y=600)
        
    def close_windows(self):
        self.master.destroy()

    def print_onscreen(self):
        self.cursor.execute("select * from student1 ")
        r=self.cursor.fetchall()
        self.l2=Label(self.master,text="Student Id",width=20,font=('Helvetica'))
        self.l2.place(x=200,y=20)
        self.l3=Label(self.master,text="Student Name",width=20,font=('Helvetica'))
        self.l3.place(x=200*2,y=20)
        self.l4=Label(self.master,text="Roll No",width=20,font=('Helvetica'))
        self.l4.place(x=200*3,y=20)
        self.l5=Label(self.master,text="Division",width=20,font=('Helvetica'))
        self.l5.place(x=200*4,y=20)
        self.l6=Label(self.master,text="Branch",width=20,font=('Helvetica'))
        self.l6.place(x=200*5,y=20)
        self.l7=Label(self.master,text="Year",width=20,font=('Helvetica'))
        self.l7.place(x=200*6,y=20)
        
        for a in range(1,10):
            for b in range(1,10):
                self.l5=Label(self.master,text="                                   ",width=400)
                self.l5.place(x=200*a,y=50*b)
        for a in range(0,len(r)):
            for b in range(0,6):
                self.l1=Label(self.master,text=r[a][b],width=20,font=('Helvetica'))
                self.l1.place(x=200*(b+1),y=90*(a+1))

#error frames
class incorrect_id:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=250,width=300)
        self.f.propagate(0)
        self.f.pack()
        self.photo_ = Image.open("error2.jpg")  
        self.photo_copy = self.photo_.copy()
        self.image_ = ImageTk.PhotoImage(self.photo_)
        self.l_p = Label(self.f, image=self.image_)
        self.l_p.bind('<Configure>', self._resize)
        self.l_p.pack(fill=BOTH, expand=YES)
        self.l1=Label(self.master,text="Incorrect Id ",font='Helvetica')
        self.l1.place(x=50,y=50)
        self.button1 = Button(self.f, text = 'OK', width = 10, command = self.close_windows,font='Courier 10',activebackground = "olive drab")
        self.button1.place(x=50,y=200)
        self.master.resizable(height=False,width=False)
    def _resize(self, event):
        self.n = event.width
        self.h = event.height
        self.photo = self.photo_copy.resize((self.n, self.h))

        self.image_ = ImageTk.PhotoImage(self.photo)
        self.l_p.configure(image=self.image_)                
    def close_windows(self):
        self.master.destroy()

class unconfirm_frame:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=200,width=400)
        self.f.propagate(0)
        self.f.pack()

        self.l1=Label(self.master,text="Cannot Issue Book , No Copies Left",font='Helvetica')
        self.l1.place(x=25,y=50)
        self.button1 = Button(self.f, text = 'OK', width = 25, command = self.close_windows,font='Courier 10',activebackground = "olive drab")
        self.button1.place(x=50,y=100)
        self.master.resizable(height=False,width=False)
                      
    def close_windows(self):
        self.master.destroy()

class enter_values:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=200,width=400)
        self.f.propagate(0)
        self.f.pack()

        self.l1=Label(self.master,text="Please Enter All Values",font='Helvetica')
        self.l1.place(x=25,y=50)
        self.button1 = Button(self.f, text = 'OK', width = 25, command = self.close_windows,font='Courier 10',activebackground = "olive drab")
        self.button1.place(x=50,y=100)
        self.master.resizable(height=False,width=False)
                      
    def close_windows(self):
        self.master.destroy()

#values added frame
class value_added:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master,height=200,width=400)
        self.f.propagate(0)
        self.f.pack()

        self.l1=Label(self.master,text="Values Have Been Added",font='Helvetica')
        self.l1.place(x=25,y=50)
        self.button1 = Button(self.f, text = 'OK', width = 25, command = self.close_windows,font='Courier 10',activebackground = "olive drab")
        self.button1.place(x=50,y=100)
        self.master.resizable(height=False,width=False)

    def close_windows(self):
        self.master.destroy()

root = Tk()
app = main_frame(root)
root.mainloop()

