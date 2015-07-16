import tornado.web

class Login(tornado.web.RequestHandler):
	def get(self):
		self.render("../views/login.html")

class Register(tornado.web.RequestHandler):
	def get(self):
		self.render("../views/register.html")