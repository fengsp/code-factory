"""
#########################################################################
wrap up widgets construction in functions for easier use, based upon some
assumptions (e.g., expansion); use **extras fkw args for width, font/color,
etc., and repack result manually later to override defaults if needed;
#########################################################################
"""

from tkinter import *

def frame(root, side=TOP, **extras):
	widget = Frame(root)
	widget.pack(side=side, expand=YES, fill=BOTH)
	if extras: widget.config(**extras)
	return widget

def label(root, side, text, **extras):
	widget = Label(root, text=text, relief=RIDGE)
	widget.pack(side=side, expand=YES, fill=BOTH)
	if extras: widget.config(**extras)
	return widget

def button(root, side, text, command, **extras):
	widget = Button(root, text=text, command=command)
	widget.pack(side=side, expand=YES, fill=BOTH)
	if extras: widget.config(**extras)
	return widget

def entry(root, side, linkvar, **extras):
	widget = Entry(root, relief=SUNKEN, textvariable=linkvar)
	widget.pack(side=side, expand=YES, fill=BOTH)
	if extras: widget.config(**extras)
	return widget

if __name__ == '__main__':
	app = Tk()
	frm = frame(app, TOP)
	label(frm, LEFT, 'SAPM')
	button(frm, BOTTOM, 'Press', lambda: print('Pushed'))
	mainloop()


