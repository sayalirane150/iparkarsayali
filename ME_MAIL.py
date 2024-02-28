"""
import smtplib

from smtplib import SMTPException

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def Submit():
    #akashgurav551@gmail.com
    # creates SMTP session  #server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    #s = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    s = smtplib.SMTP('smtp.gmail.com:587')

    m = entry_1.get()
    p = entry_2.get()
    r=  entry_3.get()
    s.login(m, p)


    #message = "...Hello Mr. .!Greetings from SMTP Protocol. This is Python Generated Mail using SMTP Module. If You receive this Message, Contact Your one of friend who is learning Python...!! \nAlso This message is Scanned and Verified by..."
    message = body.get('1.0', 'end-1c')
    try:
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.ehlo()
        s.starttls()
        s.sendmail(m,r, message)
        print("mail Sent")
        sent = tk.Label(win, text="Mail Sent Successfully !", width=20, height=4, background="black", foreground="white",
                        font=("Tempus Sans ITC", 19, "bold"))
        sent.place(x=10, y=400)

    except  (smtplib.SMTPException, ConnectionRefusedError, OSError):
        print("Mail Not Sent")
        nsent = tk.Label(win, text="Error : Mail Not Sent...Try Again !", width=20, height=4, background="black", foreground="white",
                        font=("Tempus Sans ITC", 19, "bold"))
        nsent.place(x=10, y=400)
    # terminating the session
    s.quit()


from tkinter import*
import tkinter as tk
win = tk.Tk()
win.title("Send Your Message")
win.geometry("1400x1200")
win.configure(background="turquoise1")

mail=tk.Label(win,text="Enter Your Mail",width=20,height=4,background="black",foreground="white",font=("Tempus Sans ITC",19,"bold"))
mail.place(x=0,y=0)

entry_1 = Entry(win,bd=1,width=40)
entry_1.place(x=310, y=60)

pass1=tk.Label(win,text="Enter Your Password",width=20,height=4,foreground="white",background="black",font=("Tempus Sans ITC",19,"bold"))
pass1.place(x=0,y=130)

entry_2 = Entry(win, show="*",bd=1,width=40)
entry_2.place(x=310, y=180)

Rmail=tk.Label(win,text="Enter Reciever Mail",width=20,height=4,foreground="white",background="black",font=("Tempus Sans ITC",19,"bold"))
Rmail.place(x=0,y=260)

entry_3 = Entry(win,bd=1,width=40)
entry_3.place(x=310, y=310)

body=Text(win,width=20,height=3,background="white",bd=3)
body.place(x=400,y=400)

def Browse():
    from tkinter.filedialog import askopenfilename
    fileName = askopenfilename(title='Select File To Send ',
                               filetypes=[('All files', '*.*'), ('text files', '.txt')])
    f=fileName.split("/").pop()
    q=fileName.split("/.").pop(0)
    print(q)
    print("Selected File : "+f)
    print("Selected File Path : "+fileName)

browse_file=tk.Button(win,text="Browse File",command=Browse,width=15,height=2)
browse_file.place(x=170,y=500)

submit_button=tk.Button(win,text="Submit",command=Submit,width=10,height=2)
submit_button.place(x=300,y=500)

win.mainloop()
"""
"""
from tkinter import *

root=Tk()

url = Label(root,text="Enter Url")
url.grid(row=0,padx=10,pady=10)

entry_url = Entry(root,width="50")
entry_url.grid(row=0,column=1,padx=5,pady=10,ipady=3)

root.geometry("600x300+150+150")

root.mainloop()






submit = tk.Button(win, text="Submit", command=Submit, width=25, height=2, background="purple3", foreground="snow",
                      font=("Tempus Sans ITC", 14, "bold"))
submit.place(x=30, y=350)

win.mainloop()
"""

import tkinter
from tkinter import filedialog

def main():

    tkinter.Tk().withdraw() # Close the root window
    in_path = filedialog.askopenfilename()
    print (in_path)

if __name__ == "__main__":
    main()