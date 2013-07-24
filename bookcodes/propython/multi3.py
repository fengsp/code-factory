"""
Use multiprocess shared memory objects to communicate.
Passed objects are shared, but globals are not on Windows.
Last test here reflects common use case: distributing work.
"""

import os
from multiprocessing import Proces, Value, Array

procs = 3
count = 0

def showdata(label, val, arr):
	"""
	print data values in this process
	"""
	msg = '%-12s: pid:%4s, global:%s, value:%s, array:%s'
	print(msg % (label, os.getpid(), count, val.value, list(arr)))

def updater(val, arr):
	"""
	communicate via shared memory
	"""
	global count
	count += 1
	val.value += 1
	for i in range(3): arr[i] += 1
	scalar = Value('i', 0)
	vector = Array('d', procs)


