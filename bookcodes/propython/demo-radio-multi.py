# see what happends when some buttons have some value

from tkinter import *
root = Tk()
var = StringVar()
for i in range(10):
	rad = Radiobutton(root, text=str(i), variable=var, value=str(i%3))
	rad.pack(side=LEFT)
var.set('')
root.mainloop()
