#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
6. (译)提高你的Python编码效率¶
作者:   Oz Katz
联系:   https://twitter.com/ozkatz100
翻译:   hit9
译者注: 原文链接 - http://ozkatz.github.io/
        improving-your-python-productivity.html
"""


some_list = [1, 2, 3, 4, 5]
another_list = [ x + 1 for x in some_list ]
print another_list
some_list = [1, 2, 3, 4, 5, 2, 5, 1, 4, 8]
even_set = { x for x in some_list if x % 2 == 0 }
print even_set
d = { x: x % 2 == 0 for x in range(1, 11) }
print d
myset = {1, 2, 1, 2, 3, 4}
print type(myset)
print myset
from collections import Counter
c = Counter('hello world')
print c
print c.most_common(2)
TRUE = 1
FALSE = 0
data = {"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": TRUE}, {"age": 29, "name": "Joe", "lactose_intolerant": FALSE}]}
import json
print(json.dumps(data))
print(json.dumps(data, indent=2))

from SimpleXMLRPCServer import SimpleXMLRPCServer

def file_reader(file_name):
    with open(file_name, 'r') as f:
        return f.read()

server = SimpleXMLRPCServer(('localhost', 8000))
server.register_introspection_functions()
server.register_function(file_reader)
server.serve_forever()

import xmlrpclib
proxy = xmlrpclib.ServerProxy('http://localhost:8000/')
proxy.file_reader('/tmp/secret.txt')

"""
python -m SimpleHTTPServer
"""
