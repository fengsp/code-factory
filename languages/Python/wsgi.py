#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""汉语"""
from wsgiref.handlers import CGIHandler
from wsgiref import simple_server
from beaker.middleware import SessionMiddleware

def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    return ['<html><body>Hello WSGI!</body></html>']

def show_environ(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    sorted_keys = environ.keys()
    sorted_keys.sort()
    return [
        '<html><body><h1>Keys in <tt>environ</tt></h1><p>',
        '<br/>'.join(sorted_keys),
        '</p></body></html>',
    ]

def app_session(environ, start_response):
    session = environ['beaker.session']
    if not session.has_key('value'):
        session['value'] = 0
    session['value'] += 1
    session.save()
    start_response('200 OK', [('Content-type', 'text/html')])
    return ['The current value is: %d' % session['value']]

app_session = SessionMiddleware(
    app_session,
    key='fspsession',
    secret='fspfspfsp',
)

if __name__ == '__main__':
    CGIHandler().run(application)
    print ''
    print '=' * 60
    httpd = simple_server.WSGIServer(
        ('', 8000),
        simple_server.WSGIRequestHandler,
    )
    httpd.set_app(app_session)
    httpd.serve_forever()
