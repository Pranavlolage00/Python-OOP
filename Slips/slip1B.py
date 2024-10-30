#Write Python GUI program to take accept your birthdate and output your age when a 
#button is pressed.
from tkinter import *
def disp():
    ans=t1.get()
    t2.delete(0)
    t2.insert(0,ans)
    return 
window=Tk()
window.geometry("300x300")

t1=Entry(window,width="20")
l1=Label(window,text="Enter Your BirthDate:")
l2=Label(window,text="Result:")
b1=Button(window,text="Submit",command=disp)
t2=Entry(window,width="20")

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1,column=1)
b1.grid(row=2,column=1)


