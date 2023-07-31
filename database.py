import sqlite3

class database():
    def __init__(self):
        self.connection()
        self.dastoor = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT NOT NULL , phone INTEGER);"
        self.cursor.execute(self.dastoor)
        self.dastoor = "CREATE TABLE IF NOT EXISTS factor_(id INTEGER PRIMARY KEY AUTOINCREMENT , factor INTEGER NOT NULL);"
        self.cursor.execute(self.dastoor)
        self.commit_close()
        self.insert_data(name,phone,gh_factor)
    def connection(self):
        self.conn=sqlite3.connect("aria.bling.db")
        self.cursor = self.conn.cursor()
    def commit_close(self):
        self.conn.commit()
        self.conn.close()
    def insert_data(self,name,phone,gh_factor):
        self.connection()
        self.dastoor=(f"INSERT INTO users(name,phone) VALUES ('{name}','{phone}')")
        self.cursor.execute(self.dastoor)
        self.dastoor=(f"INSERT INTO factor_(factor) VALUES ('{gh_factor}')")
        self.cursor.execute(self.dastoor)
        self.commit_close()
        self.select()
    def select(self):
        self.connection()
        self.dastoor='SELECT * from users '
        self.cursor.execute(self.dastoor)
        self.response=self.cursor.fetchall()
        for i in self.response:
            print(i)
        self.dastoor='SELECT * from factor_ '
        self.cursor.execute(self.dastoor)
        self.response=self.cursor.fetchall()
        for i in self.response:
            print(i)
        self.commit_close()
        self.update()
