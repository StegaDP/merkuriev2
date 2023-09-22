import sqlite3
import os
from dotenv import load_dotenv


class SQLite:
    def __init__(self):
        self.DB_FILE = "database.db"

        self.conn = sqlite3.connect(self.DB_FILE)
        self.cur = self.conn.cursor()

        self.cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        can_pay INTEGER,
        can_create INTEGER,
        can_approve INTEGER,
        name TEXT
    );
""")
        self.cur.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_name TEXT,
        description TEXT,
        creation_date TIMESTAMP,
        created_by INTEGER,
        pay_date TIMESTAMP,
        payed_by TEXT,
        approve_date TIMESTAMP,
        approved_by TEXT,
        message_id TEXT
    );
""")

    def commit(self):
        self.conn.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def close(self, commit=True):
        if commit:
            self.commit()
        self.conn.close()

    def execute(self, sql, params=None):
        self.cur.execute(sql, params)

    def fetchall(self):
        return self.cur.fetchall()

    def fetchone(self):
        return self.cur.fetchone()

    def query(self, sql, params=None):
        self.cur.execute(sql, params)
        return self.fetchall()