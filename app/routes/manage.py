import tornado.web
import tornado.ioloop
import tornado
import pprint
import os, uuid
from ..models.users import Users
from ..models.books import Books

__UPLOADS__ = "static/files/"

class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
		user = self.get_secure_cookie("username")
		role = self.get_secure_cookie("role")

		if role == "admin":
			if not user: return None
			return user
		else:
			self.redirect("/")
			return

class Home(BaseHandler):
	def get(self):
		if not self.current_user:
			self.redirect("/login")
			return
		self.render("../views/manage/index.html")

class ManageBooks(BaseHandler):
	def get(self):
		books_model = Books()
		books_total = books_model.count_books()
		page = 1
		try:
			page = self.get_argument("page")
		except Exception, e:
			page = 1
		offset = (int(page) - 1) * 10
		books = books_model.get_books('ID','DESC',10,offset)
		prev_page = int(page)-1
		c = int(page)*10
		r = books_total - c
		next_page = 0
		if r>0:
			next_page = int(page) + 1
		else:
		    next_page = 0
		self.render("../views/manage/books.html", books = books, next_page = next_page, prev_page = prev_page)

	def post(self):
		action = self.get_argument("action")
		
		if action=="view":
			books_model = Books()
			books = books_model.get_book(books)
			self.render("../views/manage_books.html", book=book)
		elif action=="delete":
			users_model = Users()
			user = users_model.delete_users(user)
			self.render("../views/delete_user.html", user=user)
		elif action=="edit":
			users_model = Users()
			user = users_model.edit_user(user)
			self.render("../views/edit_user.html", user=user)
		else:
			users_model = Users()
			user = users_model.add_user(user)
			self.render("../views/add_user.html", user=user)

class ManageUsers(BaseHandler):
	def get(self):
		users_model = Users()
		users_total = users_model.count_users()
		page = 1
		try:
			page = self.get_argument("page")
		except Exception, e:
			page = 1
		offset = (int(page) - 1) * 10
		users = users_model.get_users(10,offset)
		prev_page = int(page)-1
		c = int(page)*10
		r = users_total - c
		next_page = 0
		if r>0:
			next_page = int(page) + 1
		else:
		    next_page = 0
		self.render("../views/manage/users.html", users = users, next_page = next_page, prev_page = prev_page)

	def post(self):
		action = self.get_argument("action")
		
		if action=="view":
			users_model = Users()
			users = users_model.get_users(users)
			self.render("../views/view_users.html", users=users)
		elif action=="delete":
			users_model = Users()
			user = users_model.delete_users(user)
			self.render("../views/delete_user.html", user=user)
		elif action=="edit":
			users_model = Users()
			user = users_model.edit_user(user)
			self.render("../views/edit_user.html", user=user)
		else:
			users_model = Users()
			user = users_model.add_user(user)
			self.render("../views/add_user.html", user=user)

class ManageSettings(BaseHandler):
	def get(self):
		if not self.current_user:
			self.redirect("/login")
			return
		self.render("../views/manage/settings.html")

	def post(self):
		action = self.get_argument("action")