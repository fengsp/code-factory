#!/usr/bin/env python
# -*- coding: UTF-8 -*-
def foo(x, y):
    print x, y

alist = [1, 2]
adict = {'x':1, 'y':2}

foo(*alist)
foo(**adict)

x = 3
print 1 < x < 5
print 4 > x >=3

def foo(x=[]):
    x.append(1)
    print x
foo()
foo()

def foo(x=None):
    if x is None:
        x = []
    x.append(1)
    print x
foo()
foo()

for i in (1, 3, 5):
    if i % 2 == 0:
        break
else:
    print "var i is always an odd"

class Dict(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]
dct = Dict()
dct["foo"].append(1)
dct["foo"].append(2)
print dct["foo"]

from collections import defaultdict
dct = defaultdict(list)
print dct["foo"]
dct["bar"].append("Hello")
print dct

a = [1, 2, 3, 4, 5]
print a[::2]
print a[::-1]
print a[:2]

Name = "Wang" "Hone"
print Name

"""
>>> range(4)
[0, 1, 2, 3]
>>> _
[0, 1, 2, 3]
"""

import this

print [(i, j) for i in range(3) for j in range(i)]

a = [1, 2, 3, 4, 5, 6, 7]
a[1:4] = []
print a
a = [0, 1, 2, 3, 4, 5, 6, 7]
del a[::2]
print a

print isinstance(1, (float, int))
print isinstance(1.3, (float, int))
print isinstance("1.3", (float, int))

a, b = {}, {}
a['b'] = b
b['a'] = a
print a

print int(u'1234')



