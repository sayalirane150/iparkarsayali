from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
root = tk.Tk()

def browsefunc():
    filename = askopenfilename()
    pathlabel.config(text=filename)

browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()

pathlabel = Label(root)
pathlabel.pack()
root.mainloop()