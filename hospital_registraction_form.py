from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

Fullname = StringVar()
Email = StringVar()
var = IntVar()
add = StringVar()
blood = StringVar()

def database():
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
    cursor.execute('INSERT INTO Student (FullName,Email,Gender,Address,Blood_group) VALUES(?,?,?,?,?)',
                   (name1, email, gender,Address,Blood_group))
    conn.commit()


label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)

Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)


label_4 = Label(root, text="Address", width=20, font=("bold", 10))
label_4.place(x=68, y=280)

entry_4 = Entry(root)
entry_4.place(x=240, y=280)


label_5 = Label(root, text="Blood_group", width=20, font=("bold", 10))
label_5.place(x=68, y=320)

entry_5 = Entry(root)
entry_5.place(x=240, y=320)

msg = ""
print(msg)
root.destroy()
window = Tk()
window.title("Dashboard--->> " + msg)  # self.username.get() + '\n Loged In')

from subprocess import call

#call(["python", "hospital_registraction_form.py"])




#Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=240, y=420)




root.mainloop()

#
# window = Tk()
# window.title("Welcome to LikeGeeks app")
# window.geometry('550x300')
# lbl = Label(window, text="registraction form")
# lbl.grid(column=0, row=0)
# def clicked():
#     from subprocess import call
#     call(["python", "gui.py"])
#
# btn = Button(window, text="Click Me", command=clicked)
# btn.grid(column=1, row=0)
# window.mainloop()
#





















