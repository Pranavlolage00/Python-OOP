from datetime import *
from tkinter import *

def Calc():
    s1=t1.get()
    s1=s1.split("/")
    d=int(s1[0])
    m=int(s1[1])
    y=int(s1[2])
    
    dd=date.today().day
    mm=date.today().month
    yy=date.today().year
    
    dd=dd-d
    if(dd<0):
        dd=d-dd
    mm=mm-m
    if(mm<0):
        mm=m-mm
    yy=yy-y-1
    if(yy<0):
        yy=y-yy
    
    t2.insert(0,yy)
    t3.insert(0,mm)
    t4.insert(0,dd)
    return
    
window=Tk()
window.geometry("300x300")
l1=Label(window,text="Enter date:")
l2=Label(window,text="Year=")
l3=Label(window,text="Month=")
l4=Label(window,text="Day=")
b1=Button(window,text="Calculate",command=Calc)

t1=Entry(window)
t2=Entry(window)
t3=Entry(window)
t4=Entry(window)

l1.place(x=50,y=50)
l2.place(x=50,y=80)
l3.place(x=50,y=110)
l4.place(x=50,y=140)
t1.place(x=130,y=50)
t2.place(x=130,y=80)
t3.place(x=130,y=110)
t4.place(x=130,y=140)
b1.place(x=65,y=170)

window.mainloop()

