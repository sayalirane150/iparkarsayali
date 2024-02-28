import smtplib

from smtplib import SMTPException


#this app sends email  via gmail
def gmail( ):
    usermail = user_email.get()
    receivermail=receiver_email.get()
    server=smtplib.SMTP('smtp.gmail.com:587')
    pass_word=password.get()
    subject=subj.get()
    #This allow you to include a subject by adding from, to and subject line
    main_message=body.get('1.0', 'end-1c')
    Body="""From: Name here <usermail>
    To: <receivermail>
    Subject:%s 

    %s
    """% (subject, main_message)



    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(usermail, pass_word  )
        server.sendmail(usermail,receivermail, Body )

        text.insert(1.0, 'message sent')
         #error handling
    except  (smtplib.SMTPException,ConnectionRefusedError,OSError):
        text.insert(1.0, 'message not sent')
    finally:
        server.quit()





#Gui interface
from tkinter import*


root= Tk(className=" Gmail app " )
root.config(bg="brown", )

#user mail
user_email = Label(root, text="Enter your Gmail address:  ")
user_email.pack()
user_email.config(bg="black", fg="white")

user_email = Entry(root, bd =8)
user_email.pack(fill=X)


#receiver email
receiver_email = Label(root, text="Enter the recipient's email address:")
receiver_email.pack( )
receiver_email.config(bg="black", fg="white")


receiver_email = Entry(root, bd =8)
receiver_email.pack(fill=X)

#subject line
subj= Label(root, text="Enter your subject here: ")
subj.pack( )
subj.config(bg="black", fg="white")


subj = Entry(root, bd =8)
subj.pack(fill=X)







#Body of the message
body = Text(root, font="Tahoma",  relief=SUNKEN , bd=8)
body.config(bg="pink", height=15)
body.pack(fill=BOTH, expand=True)

#password widget
password = Label(root, text="Enter your Gmail password:  ")
password.pack()
password.config(bg="black", fg="white")

password= Entry(root, show='*', bd =8)
password.pack(fill=X)

#submit button
submit_mail = Button(root, bd =8, text="Click here to submit the mail",
command=gmail)
submit_mail.pack(fill=X)

#feed back
text = Text(root, font="Tahoma",  relief=SUNKEN , bd=8)
text.config(bg="pink",  height=2)
text.pack(fill=BOTH, expand=True)


root.mainloop()
