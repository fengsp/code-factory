#!/usr/bin/env python
# -*- coding: UTF-8 -*-
print abs(1.1)
print abs(-1)
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
# basestring is the superclass for str and unicode
print isinstance('fsp', basestring)
print isinstance('fsp', (str, unicode))
print bin(255)
print bool(255)
print callable(all)
print chr(97)
print cmp(1, 2)
print cmp(1, 1)
print cmp(2, 1)
print dir()
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print list(enumerate(seasons))
print isinstance(seasons, file)
class C(object):
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, x):
        self._x = x
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")
class Parrot(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
print range(10)
print range(1, 11)
print range(0, 30, 5)
print range(0, 10, 3)
print range(0, -10, -1)
print range(0)
print range(1, 0)
def myreduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduct() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value
try:
    cache
except NameError:
    cache = {}
x = [1, 2, 3]
y = [4, 5, 6]
print zip(x, y)
x2, y2 = zip(*zip(x, y))
print x2
from sys import path
import sys

