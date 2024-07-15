from tkinter import *
from tkinter import messagebox

window=Tk()
def show():
    s1=val.get()
    messagebox.showinfo("Classes",s1)
window.geometry("300x300")

r1=Radiobutton(window,text="Fy",value="FyBCA",variable=val)
r2=Radiobutton(window,text="Sy",value="SyBCA",variable=val)
r3=Radiobutton(window,text="Ty",value="TyBCA",variable=val)
b1=Button(window,text="oK",command=show)

r1.grid(row=0,column=0)
r2.grid(row=0,column=1)
r3.grid(row=0,column=2)
b1.grid(row=1,column=0)

window.mainloop()
