#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
The Python Tutorial
Python is an easy to learn, powerful programming language. It has efficient high-level 
data structures and a simple but effective approach to object-oriented programming.  
Python's elegant syntax and dynamic typing, together with its interpreted nature, 
make it an ideal language for scripting and rapid application development in many areas 
on most platforms.
The Python interpreter and the extensive standard library are freely available in source
 or binary form for all major platforms from the Python web site, http://www.python.org/,
 and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation. The Python interpreter is easily extended with new functions and data types implemented 
 in C or C++ (or other languages callable from C). Python is also suitable as an 
extension language for customizable applications.

Environment:
Python 2.7.2 (default, Oct 11 2012, 20:14:37) 
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> copyright
Copyright (c) 2001-2011 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
>>> credits
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
        for supporting Python development.  See www.python.org for more information.
"""


"""
>>> the_world_is_flat = 1
>>> if the_world_is_flat:
...     print "Be careful not to fall off!"
... 
Be careful not to fall off!
"""


"""
Error Handling
When an error occurs, the interpreter prints an error message and a stack trace. In 
interactive mode, it then returns to the primary prompt; when input came from a file, 
it exists with a nonzero exit status after printing the stack trace. (Exceptions handled 
by an except clause in a try statement are not errors in this context.) Some errors are 
unconditionally fatal and exit with a nonzero exit; this applies to internal 
inconsistnecies and some cases of running out of memory. All error messages are wirtten 
to the standared error stream; normal output from executed commands is written to a 
standard output.
Typing the interrupt charater (usually Control-C or DEL) to the primary or secondary 
prompt cancales the input and returns to primary prompt. Typing an interrupt while a 
command is executing raises the KeyboardInterrupt exception, which may be handled by a 
try statement.
"""


"""
import sys
#Python > 2.5初始化后会删除sys.setdefaultencoding function
reload(sys)
sys.setdefaultencoding('utf-8')
chinese = u"冯世鹏"
chinese_encoded = chinese.encode()
print chinese_encoded.decode()
"""


"""
The Interactive Startup File
When you use Python interactively, it is frequently handy to have some standard 
commands exexuted every time the interpreted is started. You can do this by setting 
an environment varibale named PYTHONSTARTUP to the name of a file containing your 
start-up commands. This is similar to the .profile feature of the Unix shells.

This file is only read in interactive sessions, not when Python reads commands from 
a script, and ont when /dev/tty is given as the explicit source of commands (which 
otherwise behaves like an interactive session). It is executed in the same namespace 
where interactive commands are executed, so that objects that it defines or imports 
can be used whthout qualification in the interacitive session. You can also change 
the prompts sys.ps1 and sys.ps2 in this file.

If you want to read an additional start-up file from the current directory, you can 
program this in the global start-up file using code like if os.path.isfile('
.pythonrc.py'): execfile('.pythonrc.py'). If you want to use the startup file in a 
script, you must do this explicitly in the script:
import os
filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    execfile(filename)
"""


import site
print site.getsitepackages()
print site.getusersitepackages()
