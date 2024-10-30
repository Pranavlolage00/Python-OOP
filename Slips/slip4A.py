#Write Python GUI program to create background with changing colors
from tkinter import *
window=Tk()

def Red():
    window.config(bg="red")
    return

def Green():
    window.config(bg="Green")
    return

def Blue():
    window.config(bg="Blue")
    return

window.geometry("500x500")
window.title("Changing colors")

b1=Button(text="Red",command=Red)
b2=Button(text="Green",command=Green)
b3=Button(text="Blue",command=Blue)

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)


window.mainloop()
