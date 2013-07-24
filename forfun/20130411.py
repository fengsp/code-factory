"""
Tornado web Server
"""
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


application = tornado.web.Application([
    (r"/", MainHandler),
])


# WSGI Thing
# WSGI Application is some object that is callable
def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(12))]
    start_response(status, response_headers)
    
    return [output]


class Upperware(object):
    def __init__(self, app):
        self.wrapped_app = app

    def __call__(self, environ, start_response):
        for data in self.wrapped_app(environ, start_response):
            return date.upper()


# serve(simple_app)
# serve(Upperware(simple_app))


# The WSGI application interface is implemented as a callable object: 
# a function, a method, a class or an instance with a __call__ method.
# two positional parameters:
# A dictionary containing CGI like variables; and
# a callback function that will be used by the application to send HTTP
# status code and HTTP headers to the server
# must return the response body to the server as strings wrapped in iterable.
# One application skeletion:


if __name__ == '__main__':
    # application.listen(8888)
    # tornado.ioloop.IOLoop.instance().start()
    print ''
