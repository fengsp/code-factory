import sys
from tkinter import *
from tkinter.messagebox import showinfo

class GuiMaker(Frame):
	menuBar = []
	toolBar = []
	helpButton = True

	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack(expand=YES, fill=BOTH)
		self.start()
		self.makeMenuBar()
		self.makeToolBar()
		self.makeWidgets()

	def makeMenuBar(self):
		"""
		make menu bar at the top
		"""
		menubar = Frame(self, relief=RAISED, bd=2)
		menubar.pack(side=TOP, fill=X)

		for (name, key, items) in self.menuBar:
			mbutton = Menubutton(menubar, text=name, underline=key)
			mbutton.pack(side=LEFT)
			pulldown = Menu(mbutton)
			self.addMenuItems(pulldown, items)
			mbutton.config(menu=pulldown)

		if self.helpButton:
			Button(menubar, text='Help',
					cursor = 'gumby',
					relief = FLAT,
					command = self.help).pack(side=RIGHT)
	
	def addMenuItems(self, menu, items):
		for item in items:
			if item == 'separator':
				menu.add_separator({})
			elif type(item) == list:
				for num in item:
					menu.entryconfig(num, state=DISABLED)
			elif type(item[2]) != list:
				menu.add_command(label = item[0], underline = item[1], command = item[2])
			else:
				pullover = Menu(menu)
				self.addMenuItems(pullover, item[2])
				menu.add_cascade(label = item[0], underline=item[1], menu=pullover)
	
	def makeToolBar(self):
		
