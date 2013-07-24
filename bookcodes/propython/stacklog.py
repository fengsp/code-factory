"customize stack for usage data"

from stack2 import Stack

class StackLog(Stack):
	def __init__(self, start=[]):
		pushes = 0
		pops = 0
		self.maxlen = 0
		Stack.__init__(self, start)
	
	def push(self, object):
		Stack.push(self, object)
		self.pushes += 1
		self.maxlen = max(self.maxlen, len(self))
	
	def pop(self):
		self.pops += 1
		return Stack.pop(self)
	
	def stats(self):
		return self.maxlen, self.pushes, self.pops
