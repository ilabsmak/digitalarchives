import psycopg2
import psycopg2.extensions

class Users():
    
    def get_user(self,email):
        conn = psycopg2.connect(host="139.162.202.237",database="archives",user="postgres", password="the10thguy")
        curr = conn.cursor()
        curr.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = curr.fetchall()
        return user
        
    def get_users(self, limit = 10, offset = 0):
        conn = psycopg2.connect(host="139.162.202.237", database="archives",user="postgres", password="the10thguy")
        curr = conn.cursor()
        curr.execute("SELECT * FROM users LIMIT %s OFFSET %s", (limit,offset))
        users = curr.fetchall()
        return users
        
    def count_users(self):
        conn = psycopg2.connect(host="139.162.202.237", database="archives",user="postgres", password="the10thguy")
        curr = conn.cursor()
        curr.execute("SELECT * FROM users")
        users = curr.rowcount
        return users