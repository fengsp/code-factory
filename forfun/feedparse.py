#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import feedparser

d = feedparser.parse('http://www.douban.com/feed/people/zeajin/notes')
print d['feed']['title']

rawdata = """<rss version="2.0">
<channel>
<title>Sample Feed</title>
</channel>
</rss>"""
f = feedparser.parse(rawdata)
print f['feed']['title']

rss = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
<channel>
<title>Sample Feed</title>
<description>For documentation &lt;em&gt;only&lt;/em&gt;</description>
<link>http://example.org/</link>
<pubDate>Sat, 07 Sep 2002 00:00:01 GMT</pubDate>
<!-- other elements omitted from this example -->
<item>
<title>First entry title</title>
<link>http://example.org/entry/3</link>
<description>Watch out for &lt;span style="background-image:
url(javascript:window.location='http://example.org/')"&gt;nasty
tricks&lt;/span&gt;</description>
<pubDate>Thu, 05 Sep 2002 00:00:01 GMT</pubDate>
<guid>http://example.org/entry/3</guid>
<!-- other elements omitted from this example -->
</item>
</channel>
</rss>
"""
h = feedparser.parse(rss)
print h.feed.title
print h.feed.link
print h.feed.description
print h.feed.published
print h.feed.published_parsed
print h.entries[0].title
print h.entries[0].link
print h.entries[0].description
print h.entries[0].published
print h.entries[0].published_parsed
print h.entries[0].id
