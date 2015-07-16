import os
import tornado.ioloop
import tornado.web
import routes

if __name__ == "__main__":
	static_path = os.path.join(os.path.dirname(__file__), 'static')
	settings = {
		'static_path':static_path
	}
	application = tornado.web.Application([
		(r"/", routes.index.Index),
		(r"/login", routes.users.Login),
		(r"/register", routes.users.Register),
	],**settings)
	application.listen(8888)
	tornado.ioloop.IOLoop.current().start()