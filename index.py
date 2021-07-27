from tkinter import *
import sqlite3
from tkinter import *
from tkcalendar import Calendar
from datetime import datetime
from datetime import date

import re
import sqlite3
import tkinter.messagebox
import pandas as pd

import pandas as pd
import datetime

from dateutil import rrule, parser



def login():
 root = Tk()
 root.title("Shalom Clinic")
 #width = 400
 #height = 280

 screen_width = root.winfo_screenwidth()
 screen_height = root.winfo_screenheight()
 #x = (screen_width/2) - (width/2)
 #y = (screen_height/2) - (height/2)


 root.attributes('-fullscreen', True)
 #root.geometry("%dx%d+%d+%d" % (width, height, x, y))
 root.resizable(0, 0)
#==============================METHODS========================================
 def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'shalom' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('shalom', 'admin')")
        conn.commit()
    
 def Login(event=None):
    Database()


    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:

            
            

           
            root.destroy()
        
            import mainmenu
           
           
            
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()





 def Back():
    Home.destroy()
    root.deiconify()
    
#==============================VARIABLES======================================
 USERNAME = StringVar()
 PASSWORD = StringVar()

#==============================FRAMES=========================================
 Top = Frame(root, bd=2,  relief=RIDGE)
 Top.pack(side=TOP, fill=X)
 Form = Frame(root, height=200)
 Form.pack(side=TOP, pady=20)

#==============================LABELS=========================================
 lbl_title = Label(Top, text = "Shalom Clinic", font=('arial', 15))
 lbl_title.pack(fill=X)
 lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
 lbl_username.grid(row=0, sticky="e")
 lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
 lbl_password.grid(row=1, sticky="e")
 lbl_text = Label(Form)
 lbl_text.grid(row=2, columnspan=2)

#==============================ENTRY WIDGETS==================================
 username = Entry(Form, textvariable=USERNAME, font=(14))
 username.grid(row=0, column=1)
 password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
 password.grid(row=1, column=1)

#==============================BUTTON WIDGETS=================================
 btn_login = Button(Form, text="Login", width=45, command=Login)
 btn_login.grid(pady=25, row=3, columnspan=2)
 btn_login.bind('<Return>', Login)


login()


