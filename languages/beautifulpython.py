#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    Originally From Transforming code into Beautiful, Idiomatic Python 
    by Raymond Hettinger by PyCon 2013
    Tested by fsp
"""

import os
from itertools import izip
from functools import wraps
from contextlib import contextmanager


# Looping over a range of numbers
for i in range(6):
    print i**2
for i in xrange(6): # better
    print i**2


# Looping backwards
colors = ['1', '2', '3', '4']
for color in reversed(colors):
    print color


# indicies
for i, color in enumerate(colors):
    print i, '-->', color


# Looping over two collections
names = ['asp', 'php', 'psp']
age = [10, 11, 12]

for name, age in izip(names, age):
    print name, '-->', age


# loop else
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return 1


# dict keys
d = {
    'matt': 'green',
    'rach': 'red',
    'ray': 'blue'
}
for k in d.keys():
    if k.startswith('fsp'):
        del d[k]
for k, v in d.iteritems():
    print k, '-->', v


# decorator cache
def cache(func):
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return saved[args]
        result = func(*args)
        saved[args] = result
        return result
    return newfunc

@cache
def lookup(url):
    return url

lookup('fsp')
lookup('f')
lookup('s')
lookup('p')
lookup('f')


# Ignore Exception context manager
try:
    os.remove('fsp')
except OSError:
    pass

@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

with ignored(OSError):
    os.remove('fsp')
