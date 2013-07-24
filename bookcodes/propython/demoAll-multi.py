"""
4 demo classes run as independent program processes: multiprocessing;
multiprocessing allows us to 
"""

from tkinter import *
from multiprocessing import Process
demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

def runDemo(modname):
	module = __import__(modname)
	module.Demo().mainloop()

if __name__ == '__main__':
	for modname in demoModules:
		Process(target=runDemo, args=(modname,)).start()
	
	root = Tk()
	root.title('Processes')
	Label(root, text='', bg='white').pack()
	root.mainloop()
