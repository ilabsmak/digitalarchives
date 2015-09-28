import os
import tornado.ioloop
import tornado.web
from app import routes

if __name__ == "__main__":
	static_path = os.path.join(os.path.dirname(__file__), 'static')
	settings = {
		'static_path':static_path,
		'cookie_secret':'A082935459fjonp#@#',
		'debug': True,
	}
	application = tornado.web.Application([
		(r"/", routes.index.Index),
		(r"/login", routes.users.Login),
		(r"/logout", routes.users.Logout),
		(r"/register", routes.users.Register),
		(r"/publish", routes.books.Publish),
		(r"/upload/", routes.books.Upload),
	],**settings)
	application.listen(8888)
	tornado.ioloop.IOLoop.current().start()