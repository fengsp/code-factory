import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options
define("port", default=8000, help="port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie = self.get_secure_cookie("count")
        count = int(cookie) + 1 if cookie else 1

        self.set_secure_cookie("count", str(count))
        self.write(
            '<html><head><title>Cookie Counter</title></head>' +
            '<body><h1>You&rsquo;ve viewed this page %s times.</h1>' % count +
            '</body></html>'
        )


if __name__ == "__main__":
    tornado.options.parse_command_line()

    settings = {
        "cookie_secret": "fsptest"
    }

    app = tornado.web.Application([
        (r'/', MainHandler)
    ], **settings)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

