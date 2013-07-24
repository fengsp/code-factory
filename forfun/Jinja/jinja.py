"""
Welcome
Jinja2 is a full featured template engine for Python. It has full unicode 
support, an optional integrated sandboxed execution environment, widely used 
and BSD licensed.

Jinja is Beautiful
{% extends "layout.html" %}
{% block body %}
    <ul>
    {% for user in users %}
        <li><a href="{{ user.url }}">{{ user.username }}</a></li>
    {% endfor %}
    </ul>
{% endblock %}

Jinja2 is one of the most used template engines for Python. It is inspired by 
Django's templating system but extends it with an expressive language that 
gives template authors a more powerful set of tools. On top of that it adds 
sandboxed execution and optional automatic escaping for applications where 
secrity is important.
It is internally based on Unicode and runs on a wide range of Python versions 
from 2.4 to current versions including Python 3.

Wide Range of Features
Sandboxed execution mode. Every aspect of the template execution is monitored 
and explicitly whitelisted or blacklisted, whatever is prefered. This makes it
possible to execute untrusted templates.
powerful automatic HTML escaping system for cross site scripting prevention.
Template  inheritance makes it possible to use the same or a similar layout for
all templates.
High performance with in time compilation to Python bytecode. Jinja2 will 
translate your template sources on first load into Python bytecode for best 
runtime performance.
Optional ahead-of-time compilation.
Easy to debug with a debug system that integrates template compile and runtime
errors into the standard Python traceback system.
COnfigurable syntax, For instance you can reconfigure Jinja2 to better fit 
Template designer helpers, Jinja1 ships with a wide range of useful little 
helpers that help solving common tasks in templates such as breaking up 
sequences of items into multiple columns and more.

Who is using Jinja2
Mozilla
SourceForge
Instagram
.........

Install
pip install Jinja2

More Speed with MarkupSafe
As of version 2.5.1 Jinja2 will check for an installed MarkupSafe module. 
If it can find it, it will use the Markup class of that module instead of the 
one that comes with Jinja2. MarkupSafe replaces the older speedups module that 
came with Jinja2 and has the advantage that is has a better setup script and will 
automatically attempt to install the C version and nicely fall back to a pure 
Python implementation if that is not possible.

The C implementation of MarkupSafe is much faster and recommended when using 
Jinja2 with autoescaping.
"""


from jinja2 import Template
template = Template('Hello {{ name }}!')
print template.render(name='fengsp')

