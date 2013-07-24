#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Overview
> Python design, execution model, scopes
> Python objects
> Iterators/Generators
> Decorators
> New-style class features
> Descriptors, properties
> classmethods, staticmethods
> Metaclasses, MI, Unicode
"""


# Python Desigin
# Everything is runtime(compiletime too)  (some things are cached pyc)
# Execution happens in namespaces  (modules functions classes have their own)
# Modules are executed top-to-bottom
# def and class statement are runtime
class Foo(object):
    
    def __init__(self):
        self.foo = 'foo'

foo = Foo()


def func(arg1, arg2=foo):
    print "Entering func1"
    def inner_func(arg3=arg2):
        print "entering inner_func"
        return arg1, arg3
    arg1 = arg2 = None
    return inner_func

foo.foo = 'foo2'
arg1, arg2 = func('fsp')()
print arg1, arg2.foo
# Variables are names, not containers
# Everything is an object
# Everything is a reference
# Variable are neither
# Everything concrete is an object
# Everything that holds anything, holds references
# Variables refer to objects     namespaces map names to objects
# Python Modules   Organize code
# Executed on first import        namespace becomes attributes
# Cached in sys.modules
# 'import' is syntactic sugar again    mod = __import__("mod")
os = __import__('os')
print os.path.dirname(__file__)
# Python objects
# mutability
# hashability
# usual operators + * / ** & ^ ~ += 
# Attribute access  obj.attr
# Indexing (like sequence or mapping) obj[idx]
# Calling  obj(args...)
# Iteratioin truchvalue test containment test
# for item in obj:, if obj:, if item in obj:
# Conversions   str(obj) int(obj)
# Python Classes
# All per-object data in instance attributes   stored in __dict__ attribute
# Refer to class  stored in __class__ attribute
# Attributes on class define behavior  __*__ methods
"""Iterators
Two protocols   __iter__(), next()
Not rewindable, reversable, copyable
"""
it = iter(range(10))
print zip(it, it)
"""Generators
Lazy functions that return iterators
Use yield instead of return
"""
def map(func, iterable):
    results = []
    for item in iterable:
        results.append(func(item))
    return results

def gmap(func, iterable):
    for item in iterable:
        yield func(item)
def map2(func, iterable):
    return list(gmap(func, iterable))
list1 = [1, 2, 3, 4, 5]
import math
def square(num):
    return math.pow(num, 2)
list2 = map(square, list1)
list3 = map2(square, list1)
print list2
print list3
"""Decorators
must return callables
Decorators that take extra arguments must return callables that return 
callables...
"""
from functools import wraps
def spam(repeats):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(repeats):
                func(*args, **kwargs)
        return wrapper
    return decorator

@spam(5)
def sing(line):
    """sing docstring"""
    print line
sing('fsp')
print sing.__doc__
"""New-style classes
Classic classes and instances are separate types
Lots of new general mechanisms
inherit from object
"""
"""

"""
