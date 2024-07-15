from tkinter import *
from tkinter import messagebox

def calc():
    n=t1.get()
    n=int(n)
    if val.get()==1:
        for i in range(2,n):
            if n%i==0:
                break
        if i==n-1:
            messagebox.showinfo("Alert","Number is prime")
        else:
            messagebox.showinfo("Alert","Number is Not Prime")
            
    if val.get()==2:
        s=0
        for i in range(1,n):
            if n%i==0:
                s=s+i
        if n==s:
            messagebox.showinfo("Alert","Number is perfect")
        else:
            messagebox.showinfo("Alert","Number is not perfect")

    if val.get()==3:
        n1=int(n)
        s=0
        while(n>0):
            d=n%10
            s=s+(d*d*d)
            n=n/10
            n=int(n)
        if n1==s:
            messagebox.showinfo("Alert","Number is Armstrong")
        else:
            messagebox.showinfo("Alert","Number is Not Armstrong")
    return
        
window=Tk()
window.geometry("300x300")
val=IntVar()
l1=Label(window,text="Enter Number:")
t1=Entry(window,width="20")
r1=Radiobutton(window,value=1,text="Prime",variable=val)
r2=Radiobutton(window,value=2,text="Perfect",variable=val)
r3=Radiobutton(window,value=3,text="Armstrong",variable=val)
b1=Button(window,text="Calc",command=calc)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
r1.grid(row=1,column=0)
r2.grid(row=1,column=1)
r3.grid(row=1,column=2)
b1.grid(row=2,column=0)

window.mainloop()

