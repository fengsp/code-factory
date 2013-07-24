# Frame-based menus: for top-levels and components

from tkinter import *
from tkinter.messagebox import *

def notdone():
	showerror('Not implemented', 'Not yet available')

def makemenu(parent):
	menubar = Frame(parent)
	menubar.pack(side=TOP, fill=X)

	fbutton = Menubutton(menubar, text='File', underline=0)
	fbutton.pack(side=LEFT)
	file = Menu(fbutton)
	file.add_command
