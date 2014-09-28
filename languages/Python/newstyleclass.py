#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class AClass(object):
    @staticmethod
    def astatic(): print 'a static method'

anInstance = AClass()
AClass.astatic()
anInstance.astatic()


class ABase(object):
    @classmethod
    def aclassmethod(cls): print 'a class method for', cls.__name__
class ADeriv(ABase): pass

bInstance = ABase()
dInstance = ADeriv()
ABase.aclassmethod()
bInstance.aclassmethod()
ADeriv.aclassmethod()
dInstance.aclassmethod()


class Singleton(object):
    _singletons = {}
    def __new__(cls, *args, **kwargs):
        if not cls._singletons.has_key(cls):
            cls._singletons[cls] = object.__new__(cls)
        return cls._singletons[cls]

single1 = Singleton()
single2 = Singleton()
assert id(single1) == id(single2)


class fsptest(object):
    pass

fsptest1 = fsptest()
fsptest2 = fsptest()
assert id(fsptest1) != id(fsptest2)


class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height
    area = property(getArea, doc='area of the rectangle')

rectangle = Rectangle(5, 6)
print rectangle.area


class ListNoAppend(list):
    def __getattribute__(self, name):
        if name == 'append': raise AttributeError, name
        return list.__getattribute__(self, name)

listNoAppend = ListNoAppend((1, 2, 3))
try:
    listNoAppend.append(5)
except:
    print 'exception raised'
    pass


"""A 是 B 和 C 的子类, 而 B 和 C 继承自 D,传统对象模型的的属性查找方法是 A - B - D - C - D. 由于Python先查找 D 后查找 C, 即使 C 对 D 中的方法进行了重定义, 也只能使用 D 中定义的版本. 由于这个继承模式固有的问题, 在实际应用中会造成一些麻烦."""
class A():
    def met(self):
        print 'A.met'
class B(A):
    pass
class C(A):
    def met(self):
        print 'C.met'
class D(B, C):
    pass
d1 = D()
d1.met()


# new style class
class A1(object):
    def met(self):
        print 'A1.met'
class B1(A1):
    pass
class C1(A1):
    def met(self):
        print 'C1.met'
class D1(B1, C1):
    pass
d2 = D1()
d2.met()


# super
class A2(object):
    def met(self):
        print 'A2.met'
class B2(A2):
    def met(self):
        print 'B2.met'
        super(B2, self).met()
class C2(A2):
    def met(self):
        print 'C2.met'
        super(C2, self).met()
class D2(B2, C2):
    def met(self):
        print 'D2.met'
        super(D2, self).met()
d3 = D2()
d3.met()
