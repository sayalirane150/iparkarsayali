from tkinter import *
import sqlite3
from tkinter import messagebox as ms

root = Tk()
root.geometry('500x500')
root.title("Registration Form")
root.configure(background="lemon chiffon")
Fullname = StringVar()
Email = StringVar()
var = IntVar()
add = StringVar()
blood = StringVar()

def database():
    if Fullname == None:
        Alert()
    name1 = Fullname.get()
    email = Email.get()
    gender = var.get()
    Address =add.get()
    Blood_group = blood.get()
    conn = sqlite3.connect('data.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,Address TEXT,Blood_group TEXT)')
    cursor.execute('INSERT INTO Student VALUES (Fullname,Email,Gender,Address,Blood_group) VALUES(?,?,?,?,?)',(name1, email, gender,Address,Blood_group))
    conn.commit()


label_0 = Label(root, text="Registration form",bg="snow" ,width=20, font=("Arial", 15, "bold"))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Fullname",bg="snow" , width=20, font=("Tempus Sans ITC", 15, "bold"))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=440, y=130)

label_2 = Label(root, text="Email",bg="snow" , width=20, font=("Tempus Sans ITC", 15, "bold"))
label_2.place(x=68, y=180)

entry_2 = Entry(root, textvar=Email,width=20)
entry_2.place(x=440, y=180)

label_3 = Label(root, text="Gender",bg="snow" , width=20, font=("Tempus Sans ITC", 15, "bold"))
label_3.place(x=70, y=230)

Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=440, y=230)
Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=500, y=230)


label_4 = Label(root, text="Address",bg="snow" , width=20, font=("Tempus Sans ITC", 15, "bold"))
label_4.place(x=68, y=280)

entry_4 = Entry(root)
entry_4.place(x=440, y=280)


label_5 = Label(root, text="Blood_group",bg="snow" , width=20, font=("Tempus Sans ITC", 15, "bold"))
label_5.place(x=68, y=360)

entry_5 = Entry(root)
entry_5.place(x=440, y=360)






Button(root, text='Submit', width=20,height=2, bg='green', fg='white', command=database).place(x=240, y=420)




root.mainloop()

#ms.showinfo('GoooD!', 'Username  Found.')
"""from tkinter.ttk import *
from pymsgbox import *
def Alert():
    import tkinter

    alert(text='Field Should Not Remain Entry', title='Alert', button='OK')
"""
"""
from tkMessageBox import *

root = tkinter.Tk()
def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes', 'Not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')

Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
mainloop()

Mbox = mbox.Mbox
Mbox.root = root

D = {'user':'Bob'}

b_login = tkinter.Button(root, text='Log in')
b_login['command'] = lambda: Mbox('Name?', (D, 'user'))
b_login.pack()

b_loggedin = tkinter.Button(root, text='Current User')
b_loggedin['command'] = lambda: Mbox(D['user'])
b_loggedin.pack()

root.mainloop()
"""