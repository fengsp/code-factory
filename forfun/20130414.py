"""
html5lib doc
"""
import html5lib
import urllib2
from html5lib import treebuilders
from xml.etree import cElementTree


f = urllib2.urlopen("http://www.apple.com")
doc = html5lib.parse(f)
f = urllib2.urlopen("http://www.apple.com")
doc = html5lib.parse(f, treebuilder="lxml")
parser = html5lib.HTMLParser()
f = urllib2.urlopen("http://www.apple.com")
doc = parser.parse(f)
parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("dom"))
f = urllib2.urlopen("http://www.apple.com")
minidom_docoument = parser.parse(f)
parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("etree", cElementTree))
f = urllib2.urlopen("http://www.apple.com")
etree_document = parser.parse(f)
parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("lxml"))
f = urllib2.urlopen("http://www.apple.com")
etree_document = parser.parse(f)



