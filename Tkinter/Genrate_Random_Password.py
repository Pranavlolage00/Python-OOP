from tkinter import *
from tkinter import messagebox
from random import *
from string import *
def show():
    pas=""
    for i in range(0,8):
        pas=pas+choice(ascii_letters)
    messagebox.showinfo("Random Password..",pas)
    return
window=Tk()
window.geometry("300x300")

b1=Button(window,text="Genrate Password",command=show)
b1.grid(row=1,column=0)

window.mainloop()
