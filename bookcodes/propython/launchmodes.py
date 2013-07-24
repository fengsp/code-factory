"""
#############################################################################
launch Python programs with command lines and reusable launcher scheme classes;
auto inserts "python" and/or path to Python executable at front of command line;
some of this module may assume 'python' is on your system path (see Launcher.py);

subprocess module would work too, but os.popen() uses it internally, and the goal
is to start a program running independently here, not to connect to its streams;
multiprocessing module also is an option, but this is command-lines, not functions:
doesn't make sense to start a process which would just do one of the options here;

new in this edition: runs script filename path through normpath() to change any
/ to \ for Windows tools where required; fix is inherited by PyEdit and others;
on Windows, / is generally allowded for file opens, but not by all launcher tools;
#############################################################################
"""

import sys, os
pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python'
pypath = sys.executable      # use sys in newer pys

def fixWindowsPath(cmdline):
	"""
	change all / to \ in script filename path at front of cmdline;
	used only by classes which run tools that require this on Windows;
	on other platforms, this does not hurt (e.g., os.system on Unix);
	"""
	splitline = cmdline.lstrip().split(' ')
	fixedpath = os.path.normpath(splitline[0])
	return ' '.join([fixedpath] + splitline[1:])

class LaunchMode:
	"""
	on call to instance, announce label and command;
	subclasses format command lines as required in run();
	command shoudl begin with name of the Python script
	file to run, and not with "python" or its full path;
	"""
	def __init__(self, label, command):
		self.what = label
		self.where = command
	def __call__(self):
		self.announce(self.what)
		self.run(self.where)
	def anounce(self, text):
		print(text)
	def run(self, cmdline):
		assert False, 'run must be defined'

class System(LaunchMode):
	"""
	run Python script named in shell command line
	caveat: may block caller, unless & added on Unix
	"""
	def run(self, cmdline):
		cmdline = fixWindowsPath(cmdline)
		os.system('%s %s' % (pypath, cmdline))


