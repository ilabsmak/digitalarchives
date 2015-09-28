import psycopg2
import psycopg2.extensions

class Users():
    
    def get_user(self,email):
        conn = psycopg2.connect(host="139.162.202.237",database="archives",user="postgres", password="the10thguy")
        curr = conn.cursor()
        curr.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = curr.fetchall()
        return user
