#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
More Control Flow Tools
"""


# x = int(raw_input("Please enter an integer: "))
x = 1
if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'


words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print words
print range(5, 10)
print range(0, 10, 3)
print range(-10, -100, -30)
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        print n, 'is a prime number'
for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found a number", num
class MyEmptyClass(object):
    pass
def initlog(*args):
    pass
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b
    print ''
fib(2000)
print type(fib)
f = fib
f(100)
fib(0)
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
f100 = fib2(100)
print f100
"""
The default values are evaluated at the point of function definition in the defining
scope
"""
i = 5
def f(arg=i):
    print arg
i = 6
f()
def f(a, L=[]):
    L.append(a)
    print L
f(1)
f(2)
f(3)
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print f(1)
print f(2)
print f(3)
def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese", 
           sketch="Cheese Shop Sketch")
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
print range(3, 6)
args = [3, 6]
print range(*args)
def make_incrementor(n):
    return lambda x: x+n
f = make_incrementor(42)
print f(0)
print f(1)
def my_function():
    """Do nothing, but document t.

    No really, it doesn't do anything.
    """
    pass
print my_function.__doc__


"""
Coding Style

Use 4-space indentation, and no tabs.
Wrap lines so that they do not exceed 79 characters.
Use blank lines to separate functions and classes, and larger blocks of code 
inside functions
when possible, put comments on a line of they own
use docstrings
use spaces around operators and after commas, but not directly inside 
bracketing consturct: a = f(1, 2) + g(3, 4)
Name your classes and functions consistently; the convention is to use 
CamelCase for classes and lower_case_with_underscores for functions and 
methods. Always use self as the name for the first method argument
Do not use fancy encoding if your code if meant to be used in i8n env.
Plain ASCII works best in any case.
"""



