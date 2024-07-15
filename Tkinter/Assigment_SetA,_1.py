from tkinter import *
from tkinter import messagebox

def show():
    k=messagebox.askyesno("Alert","Arer u Sure")
    if k==1:
        messagebox.showinfo("Alert","YEs Coninue")
    else:
        messagebox.showerror("ERROR","..Something Went Wrong")
        return
    
window=Tk()
window.geometry("300x300")

b1=Button(window,text="Ok",command=show)
b1.grid(row=0,column=0)

window.mainloop()

