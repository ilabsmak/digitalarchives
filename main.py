import os
import tornado.ioloop
import tornado.web
import routes

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
		(r"/register", routes.users.Register),
	],**settings)
	application.listen(8889)
	tornado.ioloop.IOLoop.current().start()