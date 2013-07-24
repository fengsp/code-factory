# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader, Template
import sys
# reload(sys)
print sys.getdefaultencoding()

env = Environment(loader=PackageLoader('app', 'templates'))
# env.trim_blocks = True
template = env.get_template('mytemplate.html')

print template.render(the='variables', go='here')

m = Template(u"{% set a, b = 'foo', 'föö' %}").module
print m.a, m.b

from jinja2 import BaseLoader, TemplateNotFound, BytecodeCache
import os

class MyLoader(BaseLoader):
    
    def __init__(self, path):
        self.path = path

    def get_source(self, environment, template):
        path = os.path.join(self.path, template)
        if not os.path.exists(path):
            raise TemplateNotFound(template)
        mtime = os.path.getmtime(path)
        with file(path) as f:
            source = f.read().decode('utf-8')
        return source, path, lambda: mtime == getmtime(path)

class MyCache(BytecodeCache):
    
    def __init__(self, directory):
        self.directory = directory

    def load_bytecode(self, bucket):
        filename = os.path.join(self.directory, bucket.key)
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                bucket.load_bytecode(f)

    def dump_bytecode(self, bucket):
        filename = os.path.join(self.directory, bucket.key)
        with open(filename, 'wb') as f:
            bucket.write_bytecode(f)

template = env.get_template('mini.html')

class navi(object):
    def __init__(self, href, caption):
        self.href = href
        self.caption = caption

navigation = []
navigation.append(navi('http://www.baidu.com', 'Baidu'))
navigation.append(navi('http://ezine.oupeng.com', 'Ezine'))
a_variable = 'a variable'
print template.render(navigation=navigation, a_variable=a_variable, escape_variable='<fsp>')

template = env.get_template('child.html')
print template.render()
"""
<ul>
{% for user in users %}
    <li>{{ user.username|e }}</li>
{% else %}
    <li><em>no users found</em></li>
{% endfor %}
</ul>
<ul class="sitemap">
{%- for item in sitemap recursive %}
    <li><a href="{{ item.href|e }}">{{ item.title }}</a>
    {%- if item.children -%
        <ul class="submenu">{{ loop(item.children) }}</ul>
    {%- endif %}</li>
{%- endfor %}
</ul>
{% if users %}
<ul>
{% for user in users %}
    <li>{{ user.username|e }}</li>
{% endfor %}
</ul>
{% endif %}
{% macro input(name, value='', type='text', size=20) -%}
{% filter upper %}
    This text becomes uppercase
{% endfilter %}
{% set navigation = [('index.html', 'Index'), ('about.html', 'About')] %}
{% set key, value = call_something() %}
{% include 'header.html' %}
    Body
{% include 'footer.html' %}
"""
template = env.get_template('macrotest.html')
print template.render(),

