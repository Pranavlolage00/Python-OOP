from tkinter import *
def add():
    a=int(t1.get())
    b=int(t2.get())
    c=a+b
    t3.insert(0,c)
    return
def sub():
    a=int(t1.get())
    b=int(t2.get())
    c=a-b
    t3.insert(0,c)
    return
def div():
    a=int(t1.get())
    b=int(t2.get())
    c=a/b
    t3.insert(0,c)
def mult():
    a=int(t1.get())
    b=int(t2.get())
    c=a*b
    t3.insert(0,c)
    return
window=Tk()
window.geometry("500x500")

l1=Label(window,text="Enter Number1:")
l2=Label(window,text="Enter Number2:")
l3=Label(window,text="Result")
t1=Entry(window)
t2=Entry(window)
t3=Entry(window)

l1.place(x=100,y=50)
l2.place(x=100,y=80)
l3.place(x=100,y=110)

t1.place(x=200,y=50)
t2.place(x=200,y=80)
t3.place(x=200,y=110)

menubar=Menu(window)

Operation=Menu(menubar)
Operation.add_command(label="Addition",command=add)
Operation.add_command(label="Subtraction",command=sub)
Operation.add_command(label="Multiplication",command=mult)
Operation.add_command(label="Division",command=div)

menubar.add_cascade(label="Operation",menu=Operation)

window.config(menu=menubar)

window.mainloop()
