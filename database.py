import sqlite3
import os

class Database:
    def __init__(self, db_name='sms.db'):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def create_table(self):
        # Create courses table
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS courses(
                cid INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                duration TEXT,
                charges TEXT,
                description TEXT
            )
        ''')
        self.con.commit()

        # Create students table
        self.cur.execute('''CREATE TABLE IF NOT EXISTS students(
            roll INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            gender TEXT,
            dob TEXT,
            contact TEXT,
            admission TEXT,
            course TEXT,
            state TEXT,
            city TEXT,
            pin TEXT,
            address TEXT
        )''')
        self.con.commit()

        # Create results table
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS results (
                rid INTEGER PRIMARY KEY AUTOINCREMENT,
                roll TEXT,
                name TEXT,
                course TEXT,
                marks TEXT,
                total_marks TEXT,
                percentage TEXT
            )
        ''')
        self.con.commit()

        # Create users table for authentication
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                uid INTEGER PRIMARY KEY AUTOINCREMENT,
                fname TEXT NOT NULL,
                lname TEXT NOT NULL,
                contact TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                security_question TEXT NOT NULL,
                security_answer TEXT NOT NULL,
                password TEXT NOT NULL,
                user_type TEXT DEFAULT 'Admin'
            )
        ''')
        self.con.commit()

    def get_conenction(self):
        return self.con, self.cur

# Initialize database
db = Database()
db.create_table()