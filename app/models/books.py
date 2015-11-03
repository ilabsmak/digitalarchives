import tornado.web
import psycopg2
import psycopg2.extensions



class Books():
    
    def add_book(self,title, excerpt, author, publisher, year, isbn, ufile):
        conn = psycopg2.connect(host="139.162.202.237",database="archives",user="postgres", password="the10thguy")
        curr = conn.cursor()
        curr.execute("INSERT INTO books(title, excerpt, author, publisher, published_date, isbn, file) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id", (title, excerpt, author, publisher, year, isbn, ufile))
        book = curr.fetchone()
        conn.commit()
        return book[0]
        
    def get_books(self, sort_column = 'ID', sort_order = 'DESC', limit = 10, offset = 0):
        conn = psycopg2.connect(host="139.162.202.237", database="archives",user="postgres", password="the10thguy")
        curr = conn.cursor()
        curr.execute("SELECT * FROM books ORDER BY %s %s LIMIT %s OFFSET %s"% (sort_column,sort_order,limit,offset))
        books = curr.fetchall()
        return books
        
    def get_book(self, book):
        conn = psycopg2.connect(host="139.162.202.237", database="archives",user="postgres", password="the10thguy")
        curr = conn.cursor()
        curr.execute("SELECT * FROM books WHERE id = %s", (book,))
        book = curr.fetchone()
        return book
        
    def search_book(self, search):
        search = search.lower()
        conn = psycopg2.connect(host="139.162.202.237", database="archives",user="postgres", password="the10thguy")
        curr = conn.cursor()
        curr.execute("SELECT * FROM books WHERE LOWER(title) LIKE '%%' || %s || '%%' OR LOWER(author) LIKE '%%' || %s || '%%'", (search, search,))
        books = curr.fetchall()
        return books
        
    def count_books(self):
        conn = psycopg2.connect(host="139.162.202.237", database="archives",user="postgres", password="the10thguy")
        curr = conn.cursor()
        curr.execute("SELECT * FROM books")
        books = curr.rowcount
        return books