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
"""Descriptors
Special objects stored in class attributes
__get__, __set__, __delete__ methods 
The mechanism behind property():
    accessors hidden behind normal attribute access
"""
class Calculate(object):
    
    def __get__(self, obj, objtype):
        return 'calculate get', obj, objtype
"""Properties
"""
class SomeClass(object):
    
    def get_prop(self):
        if not hasattr(self, '_cached_prop'):
            SomeClass._cached_prop = Calculate()
        return self._cached_prop
    prop = property(get_prop)
x = SomeClass()
print x.prop
"""Classmethods and staticmethods
instancemethods take self argument
classmethods take cls argument
staticmethods take no magic argument( not very useful)
"""
class FancyDict(dict):
    @classmethod
    def fromkeys(cls, keys, value=None):
        data = [(key, value) for key in keys]
        return cls(data)
    # So we are using decorator syntax....
    # ...or manually
    # fromkeys = classmethod(fromkeys)
MyDict = FancyDict(key1='value1', key2='value2', key3='value3')
print MyDict.fromkeys(['key1', 'key2'], 'fsp')
"""__slots__
Omit __dict__ for Python instances
Reduces memory use
Allows for immutable Python classes
"""
class Tiny(object):
    __slots__ = ['value']
    def __init__(self, value):
        self.value = value
t = Tiny(1)
print t.value
try:
    t.fsp = 'fsp'
except AttributeError, e:
    print e
"""Actual constructor(__new__)
Actual constructor method
staticmethod, not instancemethod
"""
class WrappingInt(int):
    __slots__ = []
    def __new__(cls, value):
        value = value % 255
        self = int.__new__(cls, value)
        return self
wrappingInt = WrappingInt(256)
print wrappingInt
"""Metaclasses
the class that creates a class
metacls.__new__, __init__, __getattr__
Useful for post-processing classes
Capable of much more magic (Danger)
"""
class ManglingType(type):
    def __new__(cls, name, bases, attrs):
        print cls, name, bases, attrs
        for attr, value in attrs.items():
            if attr.startswith("__"):
                continue    # avoid doing something to magical methods
            attrs["foo_" + attr] = value
            del attrs[attr]
        return type.__new__(cls, name, bases, attrs)

class MangledClass:
    __metaclass__ = ManglingType
mangledClass = MangledClass()
"""Multiple Inheritance Done Right(C3 MRO)
depth-first, left-to-right search
super() for continuing method resolution
super(ThisClass, self) returns proxy object
"""
"""Unicode
(byte)strings describe bytes
unicode describe characters
Unicode can only be stored in encoding
To get characters from bytes decode
To get bytes from characters: encode
UTF-8 can encode all of unicode
"""
# Always the Python source
