# -*- coding: utf-8 -*-
print abs(5)
print abs(-5)
print abs(-5.3)
print all((3, 0))
print all((3, 4))
print any((2, 0))
print isinstance('45', basestring)
print isinstance('5', (str, unicode))
print bin(5)
print bool(4)
print bytearray('fsp')
print callable('ha')
print chr(56)
print cmp(5, 6)
content = open('builtin_funcs.py').read()
co = compile(content, 'builtin_funcs.py', 'exec')
print co
print complex(4, 5)
obj = type.__new__(type, 'obj', (), {})
obj.fsp = 'ha'
delattr(obj, 'fsp')
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print list(enumerate(seasons))
print list(enumerate(seasons, start=1))
print eval('1+1')
print filter(lambda x: True if x % 2 == 0 else False, [1, 2, 3, 4])
print float('4.0')
print frozenset([1, 2, 3])
print hex(16)
print map(lambda x: x**2, [1, 2, 3])
print max([(0, 2), (1,)], key=len)
print oct(8)
print ord(u'冯')
print pow(2, 3)
class C(object):
    
    def __init__(self):
        self._x = None
    
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

class Parrot(object):
    
    def __init__(self):
        self._voltage = 100000

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

parrot = Parrot()
parrot.x = 'fsp'
print parrot.x
del parrot.x
print sum((4, 5))
