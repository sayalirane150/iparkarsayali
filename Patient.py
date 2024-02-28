from  tkinter import *

import sqlite3

window =Tk()
window.geometry("700x700")
window.title("PATIENT REGISTRATION FORM")
window.configure(background="lemon chiffon")
Fullname = StringVar()
address = StringVar()
bloodgroup = StringVar()
Email = StringVar()
Phoneno = StringVar()
var = IntVar()
age = StringVar()
symptoms = StringVar()
#database code
db = sqlite3.connect('source.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS empo"
               "(Fullname TEXT, address TEXT, bloodgroup TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT, symptoms TEXT)")
db.commit()


def insert():
    fname = Fullname.get()
    addr = address.get()
    bg = bloodgroup.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    sym = symptoms.get()

    conn = sqlite3.connect('source.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO empo(Fullname, address, bloodgroup, Email, Phoneno, Gender, age, symptoms) VALUES(?,?,?,?,?,?,?,?)',
                       (fname, addr,bg, email, mobile, gender, time, sym))
        db.close()

#assign and define variable

l1=Label(window,text="Registration Form",font=("Tempus Sans ITC", 15, "bold"),bg="snow")
l1.place(x=250, y=50)

#that is for label1 registration

l2 = Label(window, text="Full Name :", width=12,font=("Tempus Sans ITC", 15, "bold"),bg="snow")
l2.place(x=130, y=150)
t1 = Entry(window, textvar=Fullname,width=30)
t1.place(x=330, y=155)
# that is for label 2 (full name)


l3 = Label(window, text="Address :", width=12,font=("Tempus Sans ITC", 15, "bold"),bg="snow")
l3.place(x=130, y=200)
t2 = Entry(window, textvar=address,width=30)
t2.place(x=330, y=205)
#that is for label 3(address)

l4 = Label(window, text="blood group :", width=12,font=("Tempus Sans ITC", 15, "bold"),bg="snow")
l4.place(x=130, y=250)
t3 = Entry(window, textvar=bloodgroup,width=30)
t3.place(x=330, y=255)
#that is for label 4(blood group)

l5 = Label(window, text="E-mail :", width=12,font=("Tempus Sans ITC", 15, "bold"),bg="snow")
l5.place(x=130, y=300)
t4 = Entry(window, textvar=Email,width=30)
t4.place(x=330, y=305)
#that is for email address

l6 = Label(window, text="Phone number :", width=12,font=("Tempus Sans ITC", 15, "bold"),bg="snow")
l6.place(x=130, y=350)
t5 = Entry(window, textvar= Phoneno,width=30)
t5.place(x=330, y=355)
#phone number


l7 = Label(window, text="Gender :", width=12,font=("Tempus Sans ITC", 15, "bold"),bg="snow")
l7.place(x=130, y=400)

Radiobutton(window, text="Male", padx=5,width=5,bg="snow", font=("bold", 13), variable=var, value=1).place(x=330, y=403)
Radiobutton(window, text="Female", padx=20,width=5,bg="snow", font=("bold", 13), variable=var, value=2).place(x=405, y=403)
#gender ka natak





l8 = Label(window, text="Age :", width=12, font=("Tempus Sans ITC", 15, "bold"),bg="snow")
l8.place(x=130, y=470)
t6 = Entry(window, textvar=age,width=30)
t6.place(x=330, y=480)

#symptoms

l9 = Label(window, text="Symptoms :", width=12, font=("Tempus Sans ITC", 15, "bold"),bg="snow")
l9.place(x=130, y=520)
t7 = Entry(window, textvar= symptoms,width=30,bd=2)
t7.place(x=330, y=525)

btn= Button(window, text="Submit", bg ="black", fg = "white", width=15, height=2, command=insert)
btn.place(x=330, y=600)



window.mainloop()