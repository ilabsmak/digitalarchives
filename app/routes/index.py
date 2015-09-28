import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user = self.get_secure_cookie("username")
        if not user: return None
        return user

class Index(BaseHandler):
    def get(self):
        if not self.get_secure_cookie("log_status"):
            self.render("../views/index.html")
        else:
            self.render("../views/home.html")