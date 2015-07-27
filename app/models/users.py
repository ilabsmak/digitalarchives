import psycopg2
import psycopg2.extensions

class Users():
	def get_user(self,email):
		conn = psycopg2.connect(host="10.120.5.243",database="stuff",user="postgres", password="ilabsx")
		curr = conn.cursor()
		curr.execute("SELECT * FROM users WHERE email=%s",(email,))
		user = curr.fetchall()
		return user
