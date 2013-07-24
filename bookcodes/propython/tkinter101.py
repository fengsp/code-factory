from Tkinter import *
from Tkinter.Message import *


def reply():
	showinfo(title='popup', message='Button pressed!')

window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()
