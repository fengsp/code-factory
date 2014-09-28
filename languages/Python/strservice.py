#!/usr/bin/env python
# -*- coding: UTF-8 -*-
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
import string
print string.ascii_letters
print string.ascii_lowercase
print string.ascii_uppercase
print string.digits
print string.hexdigits
print string.letters
print string.lowercase
"""
replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
arg_name          ::=  [identifier | integer]
attribute_name    ::=  identifier
element_index     ::=  integer | index_string
index_string      ::=  <any source character except "]"> +
conversion        ::=  "r" | "s"
format_spec       ::=  <described in the next section>

"First, thou shalt count to {0}"
"Bring me a {}"
"From {} to {}"
"My quest is {name}"
"Weight in tons {0.weight}"
"Units destroyed: {players[0]}"
"Harold's a clever {0!s}"
"Bring out the holy {name!r}"
"""
print '{0}, {1}, {2}'.format('a', 'b', 'c')
print '{}, {}, {}'.format('a', 'b', 'c')
print '{2}, {1}, {0}'.format('a', 'b', 'c')
print '{2}, {1}, {0}'.format(*'abc')
print '{0}{1}{0}'.format('abra', 'cad')
print 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', 
                                            longitude='-115.81W')
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print 'Coordinates: {latitude}, {longitude}'.format(**coord)
c = 3-5j
print ('The complex number {0} is formed from the real part {0.real} and ' + \
      'imaginary part {0.imag}.').format(c)
class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)
print str(Point(4, 2))
coord = (3, 5)
print 'X: {0[0]}; Y: {0[1]}'.format(coord)
print "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
print '{:<30}'.format('left aligned')
print '{:>30}'.format('right aligned')
print '{:^30}'.format('centered')
print '{:*^30}'.format('centered')
print '{:+f}; {:+f}'.format(3.14, -3.14)
print '{: f}; {: f}'.format(3.14, -3.14)
print '{:-f}; {:-f}'.format(3.14, -3.14)
print 'int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}'.format(42)
print '{:,}'.format(1234567890)
points = 19.5
total = 22
print 'Correct answers: {:.2%}'.format(points/total)
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print '{:%Y-%m-%d %H:%M:%S}'.format(d)
for align, text in zip('<^>', ['left' 'center', 'right']):
    print '{0:{fill}{align}16}'.format(text, fill=align, align=align)
octets = [192, 168, 0, 1]
print '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
width = 5
for num in range(5, 12):
    for base in 'dXob':
        print '{0:{width}{base}}'.format(num, base=base, width=width),
    print
import re
m = re.search('(?<=abc)def', 'abcdef')
print type(m)
print m.group(0)
print re.split('\W+', 'Words, words, words.')
print re.split('(\W+)', 'Words, words, words.')
print re.split('\W+', 'Words, words, words.', 1)
print re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print m.group(0)
print m.group(1)
print m.group(2)
print m.group(1, 2)
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print m.group('first_name')
print m.group('last_name')
m = re.match(r"(..)+", "a1b2c3")
print m.group(1)
m = re.match(r"(\d+)\.(\d+)", "24.1632")
print m.groups()
m = re.match(r"(\d+)\.?(\d+)?", "24")
print m.groups()
print m.groups('0')
email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
print email[:m.start()] + email[m.end():]
from struct import *
# print pack('hhl', 1, 2, 3)
print unpack('hhl', '\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00')
print calcsize('hhl')
print calcsize('h')
print calcsize('l')
s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
from difflib import context_diff
for line in context_diff(s1, s2):
    print (line),
from difflib import unified_diff
for line in unified_diff(s1, s2):
    print (line),
"""Command line interface to difflib.py providing diffs in four formats:

* ndiff:   lists every line and highlights interline changes.
* context: highlights clusters of changes in a before/after format.
* unified: highlights clusters of changes in an inline format.
* html:    generates side by side comparison with change highlights.

"""

import sys, os, time, difflib, optparse
hlp = 'fsp help test'
def main():
    # Configure the option parser
    usage = "usage: %prog [options] fromfile tofile"
    parser = optparse.OptionParser(usage)
    parser.add_option("-c", action="store_true", default=False, help='Produce '\
                      +'a context format diff (default)')
    parser.add_option("-u", action="store_true", default=False, help='Produce a\
                             unified format diff')
    parser.add_option("-m", action="store_true", default=False, help=hlp)
    parser.add_option("-n", action="store_true", default=False,
                        help = 'Product a ndiff format diff')
    parser.add_option("-l", "--lines", type="int", default=3, help='Set \
                        number of context lines (default 3)')
    (options, args) = parser.parse_args()

    if len(args) == 0:
        parser.print_help()
        sys.exit(1)
    if len(args) != 2:
        parser.error("need to specify both a fromfile and tofile")

    n = options.lines
    fromfile, tofile = args

    fromdate = time.ctime(os.stat(fromfile).st_mtime)
    todate = time.ctime(os.stat(tofile).st_mtime)
    fromlines = open(fromfile, 'U').readlines()
    tolines = open(tofile, 'U').readlines()

    if options.u:
        diff = difflib.unified_diff(fromlines, tolines, fromfile, tofile,
                                    fromdate, todate, n=n)
    elif options.n:
        diff = difflib.ndiff(fromlines, tolines)
    elif options.m:
        diff = difflib.HtmlDiff().make_file(fromlines, tolines, fromfile,
                                    tofile, context=options.c, numlines=n)
    else:
        diff = difflib.context_diff(fromlines, tolines, fromfile, tofile, 
                                fromdate, todate, n=n)
    sys.stdout.writelines(diff)

# main()
import StringIO
import cStringIO # more efficient
output = cStringIO.StringIO()
output.write('First line.\n')
print >>output, 'Second line.'

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()
print contents,
output.close()
"""
codecs
This module defines base classes for standard Python codecs and provides access 
to the internal Python codec registry which manages the codec and error hand
 lookup process.
"""
import unicodedata
print unicodedata.lookup('LEFT CURLY BRACKET')
print unicodedata.name(u'/')
print unicodedata.decimal(u'9')
# print unicodedata.decimal(u'a')
print unicodedata.category(u'A')
print unicodedata.bidirectional(u'\u0660')

