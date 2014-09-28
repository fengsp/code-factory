"""
Classes
Compared with other programming languages.
Python's class mechanism adds classes with a minimum of new syntax 
and semantics. It is a mixture of the class mechanisms found in C++ 
and Modula-3. Python classes provide all the standard features of 
Object Oriented Programming: the class inheritance mechanism allows 
multiple base classes, a derived class can override any methods of its 
base class or classes, and a method can call the method of a base class 
with the same name. Objects can contain arbitrary amounts and kinds of 
data. As is true for modules, classes partake of the dynamic nature of 
Python: they are created at runtime, and can be modified further 

In C++ terminology, normally class members (including the data members) 
are public (except see below) and all member functions ar virtual.
As in Smalltalk, classes themselves are objects. This provides semantics 
for improving and renaming. Unlike C++ and Modula-3, built-in types can 
be used as base classes for extension by the user. Also

A Word About Names and Objects
Objects have individuality, and multiple names can be bound to the same
 object. This is known as aliasing in other languages. This is ususlly 
 not appreciated on a first glance at Python, and can be safely ignored 
 when dealing with immutable basic types(numbers, string, tuples). 
However, aliasing has a possibly surprising effect on the semantics of 
Python code invilving mutable objects such as lists, dictionaries, and 
most other types. This is usually used to the benefit of the program, 
since aliases behave like pointers in some respects,
For example passing an object is cheap since only a pointer is passed 
by the implementation; and if a function modifies an object passed as 
an argument, the caller will see the change  -----
this eliminates the need for two different argument passing mechanisms 
"""
"""
Python Scopes and Namespaces
Before introducing classes, I first have to tell you something about 
Python's scope rules. Class definitions play some neat tricks with 
namespaces, and you need to know how scopes and namespaces work to fully 
understand what's going on. Incidentally, knowledge about this subject 
is useful for any advanced Python programmer.
Let's begin with some definitions.
"""
"""
A First Look at Classes
Classes introduce a little bit of new syntax, three new object types, 
and some new semantics
"""
class MyClass(object):
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
print MyClass.__doc__
x = MyClass()
class Complex(object):
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print x.r, x.i
# There are two kinds of valid attribute names, data attributes 
# and methods.
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print x.counter
del x.counter
# In general, calling a method with a list of n arguments is equivalent 
# to calling the corresponding function with an argument list that is 
# created by inserting the method's object before the first argument
class Mapping(object):
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
    
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    __update = update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

class B(BaseException):
    pass
class C(B):
    pass
class D(C):
    pass
for c in [B, C, D]:
    try:
        raise c()
    except D:
        print "D"
    except C:
        print "C"
    except B:
        print "B"
for c in [B, C, D]:
    try:
        raise c()
    except B:
        print "B"
    except C:
        print "C"
    except D:
        print "D"
"""
Iterators
"""
for element in [1, 2, 3]:
    print element
for element in (1, 2, 3):
    print element
for key in {'one':1, 'two':2}:
    print key
for char in "123":
    print char
"""
Behind the scenes, the for elements calls the iter() on the container
the function returns an iterator object that defines the method next() 
which accesses elements in the container one at a time. when there are 
no more element, next() raises a StopIteration exception which tells 
the for loop to terminate.
"""
s = 'abc'
it = iter(s)
print it
print it.next()
print it.next()
print it.next()
try:
    print it.next()
except StopIteration:
    pass
class Reverse(object):
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
print iter(rev)
for char in rev:
    print char
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print char
"""
Operating System Interface
Standard Library
"""
import os
cwd = os.getcwd()
os.chdir('/')
print os.getcwd()
os.chdir(cwd)
# os.system('mkdir today')
import glob
print glob.glob('*.py')
import sys
print sys.argv
sys.stderr.write('Warning, log file not found starting a new one\n')
import re
print re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the hat')
print 'tea for too'.replace('too', 'two')
import math
print math.cos(math.pi / 4.0)
print math.log(1024, 2)
import random
print random.choice(['apple', 'pear', 'banana'])
print random.sample(xrange(100), 10)
print random.random()
print random.randrange(6)
import urllib2
for line in urllib2.urlopen('http://www.apple.com.cn'):
    if 'iPhone' in line:
        print line.strip()
import smtplib
"""
server = smtplib.SMTP('localhost')
server.sendmail('','','')
server.quit()
"""
from datetime import date
now = date.today()
print now
print now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
birthday = date(1991, 6, 23)
age = now - birthday
print age.days
import zlib
s = 'witch which has which witches wrist watch'
print len(s)
t = zlib.compress(s)
print len(t)
print zlib.decompress(t)
print zlib.crc32(s)
from timeit import Timer
print Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print Timer('a,b = b,a', 'a=1; b=2').timeit()
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print average([20, 30, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)

import doctest
doctest.testmod()
import unittest
class TestStatisticalFunctions(unittest.TestCase):
    
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)
unittest.main()
"""
Batteries Included
Python has a "batteries included" philosophy.
This is best seen...
xmlrpclib SimpleXMLRPCServer
email smtplib poplib
xml.dom xml.sax csv
gettext locale codecs
"""
