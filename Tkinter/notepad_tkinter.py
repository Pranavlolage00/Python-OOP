from tkinter import *

window=Tk()
window.geometry("300x300")

menubar=Menu(window)
File=Menu(menubar)
File.add_command(label="Open")
File.add_command(label="Save")
File.add_command(label="Save as")
File.add_command(label="Share")
File.add_command(label="Close")
menubar.add_cascade(label="File",menu=File)
window.config(menu=menubar)

Edit=Menu(menubar)
Edit.add_command(label="Copy")
Edit.add_command(label="Paste")
Edit.add_command(label="Cut")
Edit.add_command(label="Font")
Edit.add_command(label="Configure")
menubar.add_cascade(label="Edit",menu=Edit)
window.config(menu=menubar)

Veiw=Menu(menubar)
Veiw.add_command(label="Zoom")
Veiw.add_command(label="word wrap")
Veiw.add_command(label="status bar")
menubar.add_cascade(label="Veiw",menu=Veiw)
window.config(menu=menubar)
t1=Listbox(window,width=290)

t1.grid(row=0,column=0)
window.mainloop()
