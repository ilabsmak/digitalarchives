import tornado.web
import pprint
from ..models.users import Users

class Login(tornado.web.RequestHandler):
	def get(self):
		self.render("../views/login.html")
		
	def post(self):
		email = self.get_argument("email")
		password = self.get_argument("password")

		if not password or not email:
			self.render("../views/login.html")
		else:
			users_model = Users()
			user = users_model.get_user(email)
			pprint.pprint(user)
			self.redirect('/')

class Register(tornado.web.RequestHandler):
	def get(self):
		self.render("../views/register.html")