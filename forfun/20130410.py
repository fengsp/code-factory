"""
This file of code is the doc of Beautiful Soup 4
link: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
from bs4 import BeautifulSoup
import re


html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dorouse's story</b></p>

<p class="story">Once upon a time there were little sisters; and their names were 
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story" id="fsp">...<i>child test</i></p><b>fsptest</b>
<b><!--Comment test by fsp--></b>
"""


soup = BeautifulSoup(html_doc)
print soup.title
print soup.title.name
print soup.title.string
print soup.title.parent.name
print soup.p
print soup.p['class']
print soup.a
print soup.find_all('a')
print soup.find(id="link3")
for link in soup.find_all('a'):
    print(link['href'])
print soup.get_text()
para = soup.p
print type(para)
print para.name
print para['class']
print para.attrs
print para.string
print type(para.string)
para.string.replace_with(para.string + " replace test by fsp")
print para.string
print soup.find_all('b')[1].string
print type(soup.find_all('b')[1].string)
print soup.find_all('b')[1].prettify()
for string in soup.strings:
    print(repr(string))
title_tag = soup.title
print title_tag
print title_tag.parent
print title_tag.string.parent
link = soup.a
print link
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
print soup.find(id="fsp").next_sibling


def has_class_but_no_key(tag):
    return tag.has_key('class') and not tag.has_key('id')


print soup.find_all(has_class_but_no_key)
print soup.find(id='fsp').contents[1].string
