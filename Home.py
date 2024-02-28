from tkinter import *
import tkinter as tk
from tkinter import messagebox as ms
from tkinter.filedialog import askopenfilename


from tkinter.ttk import *
from pymsgbox import *


root=tk.Tk()

root.geometry("1400x1200")
root.configure(background="turquoise1")

def HSRG():

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
        if Fullname == None:
            Alert()
        name1 = Fullname.get()
        email = Email.get()
        gender = var.get()
        Address = add.get()
        Blood_group = blood.get()
        conn = sqlite3.connect('data.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,Address TEXT,Blood_group TEXT)')
        cursor.execute('INSERT INTO Student VALUES (Fullname,Email,Gender,Address,Blood_group) VALUES(?,?,?,?,?)',
                       (name1, email, gender, Address, Blood_group))
        conn.commit()

    label_0 = Label(root, text="Registration Form", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)

    label_1 = Label(root, text="Fullname", width=20, font=("bold", 10))
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

    Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=240, y=420)

    root.mainloop()








def Breath():
    ms.showinfo('Do Not Interrupt', 'Process May Take Much Time. Without Interrupting Wait For The Result')
    from subprocess import call
    #call(["python","C:/Users/Admin/Desktop/PROJECTS/BREATH_DETECTION/Breath_Detection.py"])

    from PIL import Image
    FI = askopenfilename(title='Select First Image for analysis ',
                    filetypes=[('All files', '*.*'), ('image files', '.jpeg')])

    SI = askopenfilename(title='Select Second Image analysis ',
                    filetypes=[('All files', '*.*'), ('image files', '.jpeg')])

    a = FI.split("/").pop()
    b = SI.split("/").pop()
    i1=Image.open(a)
    i2=Image.open(b)
    print(i1)
    #i1 = Image.open("image1.jpg")
    #i2 = Image.open("image2.jpg")
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."

    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    ncomponents = i1.size[0] * i1.size[1] * 3
    Z=(dif / 255.0 * 100)
    A=Z/ ncomponents
    print("Difference (percentage):", A)
    diff = tk.Label(root, text=str(A)+"\nAccording TO Differences\nSelect Breath-In Condition", width=35, height=3, background="VioletRed1",
                    foreground="white", font=("Tempus Sans ITC", 19, "bold"))
    diff.place(x=400, y=400)






def Mail():
    from subprocess import call
    #import pymsgbox as ms
    #ms.showinfo('MAIL PROCESS', 'Diverting To Mail Process.Yoc can Send Mail With Report To the Patient!')
    call (["python","NEW_MAIL.py"])
def Open():
    from subprocess import call

    call(["python","Open_Photo.py"])


wlcm=tk.Label(root,width=90,height=4,background="black",foreground="white",font=("Tempus Sans ITC",19,"bold"))
wlcm.place(x=0,y=0)

co=tk.Label(root,text="_________________________________Choose Options From Below_________________________________",width=100,height=2,background="turquoise1",foreground="black",font=("Tempus Sans ITC",19,"bold"))
co.place(x=0,y=150)

co=tk.Label(root,text="Contact US:\n 020 123456",width=20,height=2,background="white",foreground="black",font=("Tempus Sans ITC",19,"bold"))
co.place(x=5,y=550)

#HR=tk.Button(root,text="Hospital Registration",command=Hospital,width=25,height=3,background="purple3",foreground="snow",font=("Tempus Sans ITC",14,"bold"))
#HR.place(x=100,y=250)

mailid=str
password=str

entry_1=str
entry_2=str
#mailid = mailid.encode('utf-16')
#password = password.encode('utf-16')

mail1=tk.Button(root,text="Mail",command=Mail,width=25,height=3,background="purple3",foreground="snow",font=("Tempus Sans ITC",14,"bold"))
mail1.place(x=900,y=250)


Disease=tk.Button(root,text="Disease Detection",command=Open,width=25,height=3,background="purple3",foreground="white",font=("Tempus Sans ITC",14,"bold"))
Disease.place(x=500,y=250)

Breath=tk.Button(root,text="Breath Detection",command=Breath,width=25,height=3,background="purple3",foreground="white",font=("Tempus Sans ITC",14,"bold"))
Breath.place(x=100,y=250)


text1 = tk.Text(root, height=20, width=30)
text2 = tk.Text(root, height=20, width=50)
text=Text(root)
text.insert(INSERT,'HIII')
text.pack

root.mainloop()
