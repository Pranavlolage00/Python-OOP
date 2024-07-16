from tkinter import *

def show():
    n=t1.get()
    d={"0":"Zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
    s1=""
    for dgit in n:
        s1=s1+" "+d[dgit]
    t2.insert(0,s1)
    return

window=Tk()
window.geometry("300x300")
l1=Label(window,text="Enter Number:")
l2=Label(window,text="Result")
t1=Entry(window,width=20)
t2=Entry(window,width=20)
b1=Button(window,text="Ok",command=show)

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
b1.grid(row=2,column=0)

window.mainloop()
