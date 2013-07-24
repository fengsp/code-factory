"""
pop up three new windows, with style
destroy() kills one window, quit() kills all windows and app (ends mainloop); top-level windows have title, icon, iconify/deiconfy and protocol for wm events; there always is an application root window, whether by default or created as an explicit Tk() object; all top
"""

from tkinter import *
root = Tk()

trees = [('The larch!', 'light blue'),
	 ('The Pine!',  'light green'),
	 ('The Giant Redwood!', 'red')]

for (tree, color) in trees:
	win = Toplevel(root)
	win.title('Sing...')
	win.protocol('WM_DELETE_WINODW', lambda:None)
	win.iconbitmap('py-blue-trans-out.ico')

	msg = Button(win, text=tree, command=win.destroy)
	msg.pack(expand=YES, fill=BOTH)
	msg.config(padx=10, pady=10, bd=10, relief=RAISED)
	msg.config(bg='black', fg=color, font=('times', 30, 'bold italic'))

root.title('Lumberjack demo')
Label(root, text='Main window', width=30).pack()
Button(root, text='Quit All', command=root.quit).pack()
root.mainloop()
