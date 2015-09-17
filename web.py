import tornado.ioloop
import tornado.web
from pdf import PDF
import requests


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        title = self.get_argument('title', 'This is the title')
        circles = int(self.get_argument('circles', 10))
        lines = int(self.get_argument('lines', 10))
        pdf = PDF()
        pdf.start(title, circles, lines)
        pdf.set_title(title)
        filename = pdf.save()
        self.write(filename)
    def get(self):
        self.render('templates/page.html')




application = tornado.web.Application([
    (r"/", MainHandler),
],
    autoreload=True,
    debug=True,
    static_path='static'
)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.current().start()
