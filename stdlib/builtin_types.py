# -*- coding: utf-8 -*-
print False
print True
print None
print 0 and 1
print 0 or 1
print not 0
print 1 <= 2 <= 3
print 1 == 2
print 1 is 1
print 270 is not 270
print 1 + 2
print 2 - 1
print 1 * 2
print 1 / 2
print 1.0 // 2
print 5 % 2
print divmod(5, 2)
print 2 ** 2
print 1 | 2
print 1 ^ 2
print 1 & 2
print 1 >> 2
print 8 << 1
print -1
print 1 in (1, 2)
print 1 not in (1,)
print (1, ) + (2, )
print (1, 2) * 2
print (1, 2)[:]
print len((1, 2))
print (1, 2).index(1)
print (1, 2, 1).count(1)
print 'fsp is a student'.capitalize()
print 'fsp'.center(10)
print 'fsp'.count('f')
print 'fsp'.endswith(('s', 'p'))
print 'fsp is a student'.title()
print '%(language)s has %(number)03d quote types.' % \
      {"language": "Python", "number": 2}
print [1, 2].pop(1)
print {1, 2} < {1, 2}
print {1, 2} < {1, 2, 3}
print {1, 2} & {1}
print {1, 2} | {3}
print {1, 2}.add(3)
print {1, 2}.remove(1)
print {1, 2}.clear()
print dict(one=1, two=2, three=3)
print {'one': 1, 'two': 2, 'three': 3}
print dict(zip(['one', 'two', 'three'], [1, 2, 2]))
print dict([('two', 2), ('one', 1), ('three', 3)])
print dict({'three': 3, 'one': 1, 'two': 2})
print dict.fromkeys(('one', 'two', 'three'), 3)
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.viewkeys()
values = dishes.viewvalues()
print list(keys)
print list(values)
del dishes['eggs']
print list(keys)
print list(values)
class C:
    def method(self):
        pass
c = C()
print c.method.im_self
print c.method.im_func
print Exception
print AssertionError
print AttributeError
print EOFError
print GeneratorExit
print IOError
print ImportError
print IndexError
print KeyError
print KeyboardInterrupt
print MemoryError
print NameError
print NotImplementedError
print OSError
print RuntimeError
print StopIteration
print SyntaxError
print IndentationError
print SystemError
print TypeError
print UnicodeError
print ValueError
"""
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
      |    +-- BufferError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
       +-- ImportWarning
       +-- UnicodeWarning
       +-- BytesWarning
"""
