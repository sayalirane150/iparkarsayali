import tkinter
from PIL import Image ,ImageTk
im=Image.open(r"E:/mohit_lap_data/diease_prediction_code (1)/diease_prediction_code/medical.png")
root=tkinter.Tk()
tkimage=ImageTk.PhotoImage(im)
#a=tkinter.Label(root,image=tkimage).pack()
tkinter.Label(root,image=tkimage,text="abcdefghi",font=("Tempus Sans ITC", 30),compound=tkinter.CENTER).pack()
tkinter.Label(root,image=tkimage,text="ttttt",font=("Tempus Sans ITC", 30),compound=tkinter.LEFT).pack()
tkinter.Entry(root,width=20,).place(x=200,y=200)
root.mainloop()

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)