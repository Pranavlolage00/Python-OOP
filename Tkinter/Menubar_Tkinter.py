from tkinter import *
def color1():
    window.config(bg="pink")
    return
def color2():
    window.config(bg="red")
    return
def color3():
    window.config(bg="orange")
    return
def color4():
    window.config(bg="green")
    return 

window=Tk()
window.geometry("300x300")

menubar=Menu(window)
color=Menu(menubar)
color.add_command(label="pink",command=color1)
color.add_command(label="red",command=color2)
color.add_command(label="orange",command=color3)
color.add_command(label="Greenn",command=color4)

menubar.add_cascade(label="Color",menu=color)

window.config(menu=menubar)



window.mainloop()
