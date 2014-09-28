#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Data Structures
"""
"""
list.append(x)
Add an item to the end of the list; equivalent to a[len(a):] = [x].

list.extend(L)
Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is x. It is an error if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.index(x)
Return the index in the list of the first item whose value is x. It is an error if there is no such item.

list.count(x)
Return the number of times x appears in the list.

list.sort()
Sort the items of the list, in place.

list.reverse()
Reverse the elements of the list, in place.
"""
a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x')
a.insert(2, -1)
a.append(333)
print a
print a.index(333)
a.remove(333)
print a
a.reverse()
print a
a.sort()
print a
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print stack
print stack.pop()
print stack
print stack.pop()
print stack.pop()
print stack
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print queue.popleft()
print queue.popleft()
print queue
def f(x): return x % 2 != 0 and x % 3 != 0
print filter(f, range(2, 25))
def cube(x): return x**3
print map(cube, range(1, 11))
def add(x, y): return x+y
seq = range(8)
print map(add, seq, seq)
print reduce(add, range(1, 11))
squares = []
for x in range(10):
    squares.append(x**2)
print squares
squares = [x**2 for x in range(10)]
print squares
print [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
vec = [-4, -2, 0, 2, 4]
print [x*2 for x in vec]
print [x for x in vec if x >= 0]
print [abs(x) for x in vec]
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [num for elem in vec for num in elem]
from math import pi
print [str(round(pi, i)) for i in range(1, 6)]
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print [[row[i] for row in matrix] for i in range(4)]
print zip(*matrix)
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print a
del a[2:4]
print a
del a[:]
print a
del a
t = 12345, 54321, 'hello!'
print t[0]
print t
u = t, (1, 2, 3, 4, 5)
print u
empty = ()
singleton = 'hello',
print len(empty)
print len(singleton)
print singleton
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print fruit
print 'orange' in fruit
print 'crabgrass' in fruit
a = set('abcacadabra')
b = set('alacazam')
print a
print b
print a - b
print a | b
print a & b
print a ^ b
a = {x for x in 'abracadabra' if x not in 'abc'}
print a
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print tel
print tel['jack']
del tel['sape']
print tel
print tel.keys()
print tel.values()
print tel.items()
print 'guido' in tel
print dict([('sape', 4127), ('guido', 4127), ('jack', 4098)])
print {x: x**2 for x in (2, 4, 6)}
print dict(sape=4139, guido=4127, jack=4098)
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}? It is {1}.'.format(q, a)
for i in reversed(xrange(1, 10, 2)):
    print i
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print f
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v
words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print words
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print non_null

