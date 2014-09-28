#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pprint import pprint
import sys


# pprint(sys.path)
print False
print True
print None
print "True False Test"
print None == False
print False == False
print 0 == False
print '' == False
print () == False
print [] == False
print {} == False
if []: print 'get in'
n = -37
print bin(n)
print n.bit_length()
def my_bit_length(self):
    s = bin(self)
    s = s.lstrip('-0b')
    return len(s)
print (-2.0).is_integer()
print (3.2).is_integer()
"""
There are seven sequence types:
strings, Unicode strings, lists, tuples,
bytearrays, buffers, xrange objects
"""
print 'sTRrING'.capitalize()
print 'str'.center(10)
print 'strstrstr'.count('str', 0)
print 'fsp'.encode('utf-8')
print 'fsp'.endswith('sp')
print "The sum of 1 + 2 is {0}".format(1+2)
print '+'.join(['1', '2', '3'])
print '     spacious    '.lstrip()
print 'www.example.com'.lstrip('cmowz.')
print "they're bill's friends from the UK".title()
print '%(language)s has %(number)03d quote types.' % \
      {"language": "Python", "number": 2}
print ['fsp1', 'fsp2', 'fsp3'][0:2]
print dict(one=1, two=2, three=3)
print {'one':1, 'two':2, 'three':3}
print dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print dict([('two', 2), ('one', 1), ('three', 3)])
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.viewkeys()
values = dishes.viewvalues()
n = 0
for val in values:
    n += val
print n
print list(keys)
print list(values)
del dishes['eggs']
del dishes['sausage']
print list(keys)
n = 0
for val in values:
    n += val
print n
print keys & {'eggs', 'bacon', 'salad'}
class C:
    def method(self):
        pass
c = C()
c.method.im_func.whoami = 'my name is method'
print c.method.whoami

