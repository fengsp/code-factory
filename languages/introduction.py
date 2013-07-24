#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
An Informal Introduction to Python
"""
# Example #
# this is the first comment
SPAM = 1                # and this is the second comment
                        # ... and now a third
STRING = "# This is not a comment."
print 2+2
print (50-5*6)/4
print 7/3
print 7/-3
width = 20
height = 5*9
print width * height
x = y = z = 0
print 3 * 3.75 / 1.5
print 7.0 / 2
print 1j * 1J
print 1j * complex(0, 1)
print 3+1j*3
print (3+1j)*3
print (1+2j)/(1+1j)
a = 1.5+0.5J
print a.real
print a.imag
a = 3.0+4.0j
print abs(a)
from math import sqrt
assert(abs(a), sqrt(a.real**2 + a.imag**2))
tax = 12.5 / 100
price = 100.50
print price * tax
# print price + _      IN interactive mode, the last printed expression is assigned to 
# print round(_, 2)    the variable _.
print 'spam eggs'
print 'doesn\'t'
print "doesn't"
print '"Yes," he said.'
print "\"Yes,\" he said."
print '"Isn\'t she said.'
print "This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
    Note that whitespace at the begining of the line is\
 significant."
print """
Usage: thingy [OPTIONS]
     -h                     Display this usage message
     -H hostname            Hostname to connect to
"""
print r"This is a rather long string containing\n\
several lines of text much as you would do in C."
word = 'Help' + 'A'
print word
print '<' + word*5 + '>'
print 'str' 'ing'
print 'str'.strip() + 'ing'
print word[4]
print word[0:2]
print word[2:4]
print word[:2]
print word[2:]
print 'x' + word[1:]
print 'Splat' + word[4]
print word[:2] + word[2:]
print word[:3] + word[3:]
print word[1:100]
print word[10:1]
print word[2:1]
print word[-1]
print word[-2]
print word[-2:]
print word[:-2]
print word[-0]
print word[-100:0]
s = 'supercalifragilisticexpialidocious'
print len(s)
print u'Hello World !'
print u'Hello\u0020World !'
print ur'Hello\u0020World !'
print ur'Hello\\u0020World !'
print ur'Hello\\\u0020World !'


"""
When a Unicode string is printed, written to a file, or converted with str(), 
conversion takes place using this default encoding.
"""
print u"abc"
print str(u"abc")
print u"äöü"
print u"äöü".encode('utf-8')
print unicode('\xc3\xa4\xc3\xb6\xc3\xbc', 'utf-8')
a = ['spam', 'eggs', 100, 1234]
print a
print a[0]
print a[3]
print a[-2]
print a[1:-1]
print a[:2] + ['bacon', 2*2]
print 3*a[:3] + ['Boo!']
print a[:]


"""
Unlike strings, which are immutable, it is possible to change individual elements of 
a list:
Assignment to slices is also possible, and this even change the size of the list or
clear it entirely:
"""
print a
a[2] = a[2] + 23
print a
a[0:2] = [1, 12]
print a
a[0:2] = []
print a
a[1:1] = ['bletch', 'xyzzy']
print a
a[:0] = a
print a
a = ['a', 'b', 'c', 'd']
print len(a)
q = [2, 3]
p = [1, q, 4]
print len(p)
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b<10:
    print b
    a, b = b, a+b
i = 256*256
print 'The value of i is', i

