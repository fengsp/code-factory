"""
Some web.py thing
http://webpy.org/docs/
"""
import web


urls = (
    '/', 'index'
)


class index:
    def GET(self):
        render = web.template.render('../Jinja/app/templates/')
        # name = 'fsp'
        i = web.input(name=None)
        return render.index(i.name)
        # return "Hello, world!"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
