#Write a Python GUI program to create a label and change the label font style (font 
#name, bold, size) using tkinter module.
from tkinter import *
def Font():
    l1.config(font=("Dubai","20","bold"))
    return
def Size():
    l1.config(font=("Dubai","50"))
    return
def Bold():
    l1.config(font=("bold","20"))
    return

window=Tk()
window.geometry("300x300")
l1=Label(window,text="Wel-come To Python")
r1=Radiobutton(window,text="Font",command=Font,value=1)
r2=Radiobutton(window,text="Size",command=Size,value=2)
r3=Radiobutton(window,text="Bold",command=Bold,value=3)

l1.place(x=100,y=50)
r1.place(x=0,y=80)
r2.place(x=0,y=110)
r3.place(x=0,y=140)
window.mainloop()
