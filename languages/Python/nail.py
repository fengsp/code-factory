#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""A python web framework called nail
   Never reinvent the wheel
"""

# model.py
from sqlalchemy import Table, Column, String
import dbconfig

entry_table = Table('entry', dbconfig.metadata,
                    Column('id', String(100), primary_key=True),
                    Column('title', String(100)),
                    Column('content', String(30000)),
                    Column('updated', String(20), index=True))

# dbconfig.py
from sqlalchemy import *

metadata = BoundMetaData('sqlite://tutorial.db')

# manage.py
import os, sys

def create():
    from sqlalchemy import Table
    import model
    for (name, table) in vars(model).iteritems():
        if isinstance(table, Table):
            table.create()

def run():
    import urls
    if os.environ.get("REQUEST_METHOD", ""):
        form wsgiref.handlers import BaseCGIHandler
        BaseCGIHandler(sys.stdin, sys.stdout, sys.stderr, os.environ).run(
                                            urls.urls)
    else:
        form wsgiref.simple_server import WSGIServer, WSGIRequestHandler
        httpd = WSGIServer(('', 8080), WSGIRequestHandler)
        httpd.set_app(urls.urls)
        print "Serving HTTP on %s port %s ..." % httpd.socket.getsockname()
        httpd.serve_forever()

# add the following so that command works:
# $ python manage.py create
if __name__ == "__main__":
    if 'create' in sys.argv:
        create()
    if 'run' in sys.argv:
        run()
# Some tests
# $python
# >>> import model
# >>> i = model.entry_table.insert()
# >>> i.execute(id='first-post', title="Some Title", content="Some pithy text...", updated="2006-09-01T01:00:00Z")
# >>> i.execute(id='second-post', title="Moving On", content="Some not so pithy words...", updated="2006-09-01T01:01:00Z")

# urls.py
import selector
import view

urls = selector.Selector()
urls.add('/blog/', GET=view.lists)
urls.add('/blog/{id}/', GET=view.memeber_get)
urls.add('/blog/;create_form', POST=view.create, GET=view.lists)
urls.add('/blog/{id}/;edit_form', GET=view.member_get, POST=view.member_update)

# view.py
import nail
import model

def lists(environ, start_response):
    rows = model.entry_table.select().execute()
    return nail.render(start_response, 'list.html', locals())

def member_get(environ, start_response):
    id = environ['selector.vars']['id']
    row = model.entry_table.select(model.entry_table.c.id==id).execute().fetchone()
    return nail.render(start_response, 'entry.html', locals())

def create(environ, start_response):
    pass
def create_form(environ, start_response):
    pass
def member_edit_form(environ, start_response):
    pass
def member_update(environ, start_response):
    pass

# nail.py
import kid
import os

extensions = {
    'html': 'text/html',
    'atom': 'application/atom+xml'
}

def render(start_response, template_file, argus):
    ext = template_file.rsplit(".")
    contenttype = 'text/html'
    if len(ext) > 1 and (ext[1] in extensions):
        contenttype = extensions[ext[1]]
    template = kid.Template(file=os.path.join('templates', template_file), **argus)
    body = template.serialize(encoding='utf-8')
    start_response("200 OK", [('Content-type', contenttype)])
    return [body]

# list.html
<?xml version="1.0" encoding="utf-8"?>
<html xmlns:py="http://purl.org/kid/ns#>">
<head>
    <title>A Robaccia Blog</title> 
</head>
<div py:for="row in rows.fetchall()">
    <h2>${row.title}</h2>
    <div>${row.content}</div>
    <p><a href="./${row.id}/">${row.updated}</a></p>
</div>
</html>

