from torngas.handler import WebHandler


class BaseHandler(WebHandler):
    """
    do some your base things
    """


class Main(BaseHandler):
    def get(self):
        welcome = "Hello,Torngas!"
        self.render("index.html", welcome=welcome)
