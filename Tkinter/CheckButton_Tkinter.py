from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("300x300")
def show():
    s=""
    if a1.get()==1:
        s="Java"
    if a2.get()==1:
        s=s+"PHP"
    if a3.get()==1:
        s=s+".Net"
    t1.insert(0,"")
    messagebox.showinfo("Information",s)
    t1.insert(0,s)  
    return
a1=IntVar()
a2=IntVar()
a3=IntVar()

t1=Entry(window,width=20)
c1=Checkbutton(window,text="Java",variable=a1)
c2=Checkbutton(window,text="Php",variable=a2)
c3=Checkbutton(window,text=".Net",variable=a3)
b1=Button(window,text="OK",command=show)

c1.grid(row=0,column=0)
c2.grid(row=0,column=1)
c3.grid(row=0,column=2)
t1.grid(row=1,column=0)
b1.grid(row=2,column=0)

window.mainloop()



