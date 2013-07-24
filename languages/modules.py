#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Modules
A module is a file containing Python definitions and statements. Within a 
module, the module's name is available as the value of the global variable 
__name__.
"""


"""
The Module Search Path
When a module named spam is imported, the interpreter first searches for a 
build-in module with that name. If not found, it then searches for a file 
named spam.py in a list of directories given by the variable sys.path.
sys.path is initialized from these locations:
* the directory containing the input script(or the current directory).
* PYTHONPATH(a list of directory names, with the same syntax as the shell 
  variable PATH.)
* the installation-dependent default.

After initialization, Python programs can modify sys.path. The directory 
containing the script being run is placed at the beginning of the search path,
ahead of the standard library path. This means that script in that directory 
will be loaded instead of modules of the same name in the library directory. 
This is an error unless the replacement is intended. See section Standard 
Modules for more information.
"""


"""
Compiled Python files
As an important speed-up of the start-up time for short programs that use a 
lot of standard modules, if a file called spam.pyc exists in the directory 
where spam.py is found, this is assumed to contain an already- "byte-compiled"
version of the module spam. The modification time of the version of spam.py 
used to create spam.pyc is recorded in spam.pyc, and the .pyc file is ignored 
if these don't match.

Normally, you do not need to do anything to create the spam.pyc file. Whenever
spam.py is successfully compiled, an attempt is made to write the compiled 
version to spam.pyc. It is not an error if this attempt fails; if for any 
reason the file is not written completely, the resulting spam.pyc file will be
invalid. The contents of the spam.pyc file are platform independent, so a 
Python module directory can be shared by machines of different archiectures.

A program doesn't run any faster when it is read from a .pyc and .pyo file 
than when it is read from a .py file; the only thing that's faster about .pyc 
or .pyo files is the speed with which they are loaded.

When a script is run by giving its name on the command line, the bytecode for the script is never written to a .pyc or .pyo file. Thus, the startup time of a script may be reduced by moving most of its code to a module and having a small bootstrap script that imports that module. It is also possible to name a .pyc or .pyo file directly on the command line.

The module compileall can create .pyc files (or .pyo files when -O is used) for all modules in a directory.
"""


"""
Standard Modules

Python comes with a library of standard modules, described in a separate doc, 
"""


"""
The dir() Function
The build-in function dir is used to find out which names a module defines. It
returns a sorted list of strings:
"""

import sys
from pprint import pprint
pprint (dir(sys))
pprint (dir())
import __builtin__
pprint (dir(__builtin__))

"""
Packages

When importing the package, Python searches through the directories on 
sys.path looking for the package subdirectory.
The __init__.py files are required to make Python treat the directories as 
containing packages; this is done to prevent directories with a common name

Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last must be a package; the last item can be a module or a package but can’t be a class or function or variable defined in the previous item.

you can contain the following code in __init__.py file
__all__ = ["echo", "surround", "reverse"]

If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package sound.effects into the current namespace; it only ensures that the package sound.effects has been imported (possibly running any initialization code in __init__.py) and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by __init__.py. It also includes any submodules of the package that were explicitly loaded by previous import statements. 
"""
s = 'Hello, world.'
print str(s)
print repr(s)
print str(1.0/7.0)
print repr(1.0/7.0)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print s
hello = 'hello, world\n'
hellos = repr(hello)
print hello
print hellos
for x in range(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3),
    print repr(x**3).rjust(4)
for x in range(1, 11):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3)
print '{0} and {1}'.format('spam', 'eggs')
print '{1} and {0}'.format('spam', 'eggs')
print 'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')
print 'The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other=\
                                                            'Georg')
import math
print 'The value of PI is approximately {}.'.format(math.pi)
print 'The value of PI is approximately {!r}.'.format(math.pi)
print 'The value of PI is approximately {0:.3f}.'.format(math.pi)
table = {'Sjoerd': 4127, 'Jack':4098, 'Dcab': 7678}
for name, phone in table.items():
    print '{0:10} ==> {1:10d}'.format(name, phone)
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print ('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
       'Dcab: {0[Dcab]:d}'.format(table))
print 'The value of PI is approximately %5.3f.' % math.pi
f = open('workfile', 'r')
print f
print f.read()
f = open('workfile', 'r')
print f.readline(),
print f.readline(),
print f.readline()
for line in f:
    print line
f = open('workfile', 'r+')
f.write('0123456789abcdef')
print repr(f.read())
f.seek(5)
print f.read(1)
f.seek(-3, 2)
print f.tell()
print f.read(1)
f.close()

