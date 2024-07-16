from tkinter import *
def show():
    n=int(t1.get())
    b=bin(n)
    o=oct(n)
    h=hex(n)
    t2.insert(0,b)
    t3.insert(0,o)
    t4.insert(0,h)
    return
        
window=Tk()
window.geometry("300x300")

l1=Label(window,text="Enter Number:")
l2=Label(window,text="Binary:")
l3=Label(window,text="Octal:")
l4=Label(window,text="Hexa:")
t1=Entry(window,width=20)
t2=Entry(window,width=20)
t3=Entry(window,width=20)
t4=Entry(window,width=20)
b1=Button(window,text="Ok",command=show)

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
l4.grid(row=3,column=0)

t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
t3.grid(row=2,column=1)
t4.grid(row=3,column=1)

b1.grid(row=4,column=0)

window.mainloop()
