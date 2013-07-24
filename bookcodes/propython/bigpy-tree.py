"""
Find the largest Python source file in an entile directory tree.
Search the Pytho source lib, use pprint to display results nicely.
"""

import sys, os, pprint
trace = False
if sys.platform.startswith('win'):
	dirname = r"C:"
else:
	dirname = '/'

allsizes = []
for (dirname, subs, files) in os.walk(dirname):
	if trace: print(dirname)
	for filename in files:
		if filename.endswith('.py'):
			if trace: print('...', filename)
			fullname = os.path.join(dirname, filename)
			fullsize = os.path.getsize(fullname)
			allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
