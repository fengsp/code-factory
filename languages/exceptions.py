#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Errors and Exceptions
"""
"""
>>> while True print 'Hello world'
  File "<stdin>", line 1
      while True print 'Hello world'
                         ^
                         SyntaxError: invalid syntax
"""


"""
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ZeroDivisionError: integer division or modulo by zero
  >>> 4 + spam*3
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'spam' is not defined
    >>> '2' + 2
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      TypeError: cannot concatenate 'str' and 'int' objects
"""


while True:
    try:
        x = 1    # int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Oops! That was no valid number. Try again..."


"""
The try statement works as follows:
* First the try clause between the try and except is executed
* If no exception occurs, the except clause if skipped
* If an exception occurs, the rest of the clause if skipped
  Then if its type matches the exception named after except keywork, the 
  except clause is executed, and then execution continues after the try
  statement.
* If an exception occurs which does not match the exception named in the 
  except clause, it is passed to outer try statements; if no handler is found.
  it is an unhandled exception and execution stops with a message as shown
* except (RuntimeError, TypeError, NameError):
      pass
"""


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexcepted error:", sys.exc_info()[0]
    raise
else:
    print "myfile.txt has", len(f.readlines()), 'lines'
    f.close


try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    try:
        print type(inst)
        print inst.args
        print inst
        x, y = inst.args
        print 'x=', x
        print 'y=', y
        print inst.errno
        print inst.strerror
    except AttributeError as e:
        pass
def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDivisionError as detail:
    print 'Handling run-time error:', detail
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as e:
    print 'My exception occurred, value:', e.value
class Error(Exception):
    """Base class for exception in this module."""
    pass
class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        prev -- state at begining of transition
        next -- attempted new state
        msg  -- explanation of why the specific transition is not allowed
    """

    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg
try:
    raise KeyboardInterrupt
except:
    pass
finally:
    print 'Goodbye, world!'
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    else:
        print "result is", result
    finally:
        print "Executing finally clause"
divide(9, 3)
divide(9, 0)
try:
    with open("myfile.txt") as f:
        for line in f:
            print line,
except IOError as e:
    print e.strerror
