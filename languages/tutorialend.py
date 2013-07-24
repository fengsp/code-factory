"""
Brief Tour of the Standard Library - PART II
"""
import repr
print repr.repr(set('supercalifragilisticexpialidocious'))
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
        'yellow'], 'blue']]]
pprint.pprint(t)
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print textwrap.fill(doc, width=40)
import locale
print locale.format("%d", 1234567.8, grouping=True)
from string import Template
t = Template('${village}fork send $$10 to $cause.')
print t.substitute(village='Nottingham', cause='the ditch fund')
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
try:
    print t.substitute(d)
except KeyError:
    pass
print t.safe_substitute(d)

import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
# fmt = raw_input('Enter rename style (%d-date %n-seqnum %f-format): ')
fmt = 'fsp_%n%f'
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print '{0} --> {1}'.format(filename, newname)
import struct
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print d['primary']
del a
print gc.collect()
try:
    print d['primary']
except KeyError:
    print 'keyError'
from array import array
a = array('H', [4000, 10, 700, 22222])
print sum(a)
print a[1:3]
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append('task4')
print "Handling", d.popleft()
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
print [heappop(data) for i in range(3)]
from decimal import *
x = Decimal('0.70') * Decimal('1.05')
print x
print x.quantize(Decimal('0.01'))
print round(.70 * 1.05, 2)
print Decimal('1.00') % Decimal('.10')
print 1.00 % 0.10
print sum([Decimal('0.1')]*10) == Decimal('1.0')
print sum([0.1]*10) == 1.0
getcontext().prec = 36
print Decimal(1) / Decimal(7)

