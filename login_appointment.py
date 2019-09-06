from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import ImageTk,Image

with sqlite3.connect('database1.db') as db:
    c = db.cursor()

db.commit()
db.close()

class main:
    def __init__(self,master):
    
        self.master = master
       
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        
        self.widgets()

    def login(self):
        with sqlite3.connect('database1.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            top=Toplevel()
            top.title("appointment window")
          
            top.left = Frame(top, width = 850 ,height = 750)
            top.left.pack(side=LEFT)
            #top.right = Frame(top, width = 200 ,height = 720, bg = 'steelblue')
            #top.right.pack(side=RIGHT)
            top.image=ImageTk.PhotoImage(Image.open("hospital4.jpg"))
            top.panel=Label(top.left,image=top.image)
            top.panel.pack()

            top.heading = Label(top.left,text="vivekanand Hospital",font=('arial 40 bold'),bd=3,fg='black')
            top.heading.place(x=135,y=0)

            top.name = Label(top.left,text="patient's_name",font=('arial 18 bold'),bd=3,fg='black')
            top.name.place(x=0,y=100)

            top.age = Label(top.left,text="Age",font=('arial 18 bold'),fg='black')
            top.age.place(x=0,y=140)

            top.gender = Label(top.left,text="Gender",font=('arial 18 bold'),fg='black')
            top.gender.place(x=0,y=180)

            top.address = Label(top.left,text="Address",font=('arial 18 bold'),fg='black')
            top.address.place(x=0,y=220)

            top.location = Label(top.left,text="phone",font=('arial 18 bold'),fg='black')
            top.location.place(x=0,y=480)

            top.time = Label(top.left,text="Time",font=('arial 18 bold'),fg='black')
            top.time.place(x=0,y=520)

            def next():
                top.val1=top.name_ent.get()
                top.val2=top.age_ent.get()
                top.val3=top.gender_ent.get()
                top.val4=top.address_ent.get("1.0",'end-1c')
                top.val5=top.location_ent.get()
                top.val6=top.time_ent.get()

                if(top.val1=='' or top.val2=='' or top.val3=='' or top.val4=='' or top.val5=='' or top.val6==''):
                   ms.showinfo("warning","fill all the required details")
                else:
                    sqlite3.connect('database1.db')
                    sql="INSERT INTO 'appointment'(name,age,gender,address,phone,time)VALUES(?,?,?,?,?,?)"
                    c.execute(sql,(top.val1,top.val2,top.val3,top.val4,top.val5,top.val6))
                    db.commit()
                    ms.showinfo( "Success","appointment been recorded")

            top.name_ent=Entry(top.left,width=30,bd=3)
            top.name_ent.place(x=250,y=100)

            top.age_ent=Entry(top.left,width=30,bd=3)
            top.age_ent.place(x=250,y=140)

            top.gender_ent=Entry(top.left,width=30,bd=3)
            top.gender_ent.place(x=250,y=180)

            top.address_ent=Text(top.left,width=40,height=15)
            top.address_ent.place(x=250,y=220)

            top.location_ent=Entry(top.left,width=30,bd=3)
            top.location_ent.place(x=250,y=480)

            top.time_ent=Entry(top.left,width=30,bd=3)
            top.time_ent.place(x=250,y=520)

            top.next=Button(top.left,text="Next",width=20,height=2,bg='red',bd=3,command=next)
            top.next.place(x=250,y=560)

        else:
            ms.showerror('Oops!','invalid credentials.')
            
    def new_user(self):
        
        with sqlite3.connect('database1.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log() 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
    
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)


root = Tk()
root.title("Login page")
main(root)
root.mainloop()
