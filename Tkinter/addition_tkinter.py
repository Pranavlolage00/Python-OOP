import tkinter as t
def Calc():
    a=t1.get()
    b=t2.get()
    a=int(a)
    b=int(b)
    c=a+b
    t3.delete(0,t.END) # it is remove Existing text from the Entry..
    t3.insert(0,c) #insert value / set Value
    return

window=t.Tk()
window.geometry("300x300")
l1=t.Label(window,text="Enter Number1:")
l2=t.Label(window,text="Enter Number2:")
t1=t.Entry(window,width="20")
t2=t.Entry(window,width="20")
l3=t.Label(window,text="Result:")
t3=t.Entry(window,width="20")
b1=t.Button(window,text="Calc",command=Calc)

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
l3.grid(row=2,column=0)
t3.grid(row=2,column=1)
b1.grid(row=3,column=1)

window.mainloop()
