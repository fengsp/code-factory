gifdir = '../gifs/'
from tkinter import *
win = Tk()
igm = PhotoImage(file=gifdir + 'fsp.gif')
Button(win, image=igm).pack()
win.mainloop()
