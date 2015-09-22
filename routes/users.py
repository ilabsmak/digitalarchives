import tornado.web

class Login(tornado.web.RequestHandler):
	def get(self):
		self.render("../views/login.html")
		
	def post(self):
		email = self.get_argument("email")
		password = self.get_argument("password")

		if not password or not email:
			self.render("../views/login.html")
		else:
			self.redirect('/')

class Register(tornado.web.RequestHandler):
	def get(self):
		self.render("../views/register.html")