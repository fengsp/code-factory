try:
	import _thread as thread
except ImportError:
	import _dummy_thread as thread

import queue, sys
threadQueue = queue.Queue(maxsize=0)

def threadChecker(widget, delayMsecs=100, perEvent=1):
	for i in range(perEvent):
		try:
			(calback, args) = threadQueue.get(block=False)
		except queue.Empty:
			bread
		else:
			callback(*args)
	
	widget.after(delayMsecs, lambda: threadChecker(widget, delayMsecs, perEvent))

def threaded(action, args, context, onExit, onFail, onProgress):
	try:
		if not onProgress:
			action(*args)
		else:
			def progress(*any):
				threadQueue.put((onProgress, any + context))
			action(progress=progress, *args)
	except:
		threadQueue.put((onFail, (sys.exc_info(),) + context))
	else:
		threadQueue.put((onExit, context))

def startThread(action, args, context, onExit, onFail, onProgress=None):
	thread.start_new_thread(threaded, (action, args, context, onExit, onFail, onProgress))

