import tkinter as tk

def add():
    val=t1.get()
    t1.insert(0,"")
    lst.insert(0,val)
    return

def Clear():
    pos=lst.curselection()
    lst.delete(pos)
    return

def Clear_All():
    lst.delete(0,lst.size())
    return

window=tk.Tk()
window.geometry("300x300")

l1=tk.Label(window,text="Enter Product:")
l2=tk.Label(window,text="All Product-")

t1=tk.Entry(window, width="20")

lst=tk.Listbox(window, width="10")

b1=tk.Button(window,text="Add",command=add)
b2=tk.Button(window,text="Clear",command=Clear)
b3=tk.Button(window,text="Clear All",command=Clear_All)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)

l2.grid(row=1,column=0)
lst.grid(row=1,column=1)

b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)

window.mainloop()
