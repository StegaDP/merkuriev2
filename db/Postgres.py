import os

import sqlite3
from dotenv import load_dotenv


class SQLite:
    def __init__(self):
        # load_dotenv("../.env")
        # env = os.environ
        # self.DB_NAME = env.get("DB_NAME")
        # self.DB_HOST = env.get("DB_HOST")
        # self.DB_USER = env.get("DB_USER")
        # self.DB_PASSWORD = env.get("DB_PASSWORD")
        # self.DB_PORT = env.get('DB_PORT')
        self.conn = sqlite3.connect(
            'database.db'
            # f"host='{self.DB_HOST}' port='{self.DB_PORT}' dbname='{self.DB_NAME}' user='{self.DB_USER}' password='{self.DB_PASSWORD}'"
        )
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users(\
                id INT PRIMARY KEY,\
                can_pay INT,\
                can_create INT,\
                can_approve INT,\
                name TEXT);\
                ")
        self.cur.execute("CREATE TABLE IF NOT EXISTS reports(\
                created_by INT PRIMARY KEY,\
                document_name TEXT,\
                description TEXT,\
                creation_date TEXT,\
                approve_date TEXT,\
                pay_date TEXT,\
                approved_by INT,\
                payed_by INT,\
                message_id INT);\
                ")
        self.commit()

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
        self.cur.execute(sql, params or ())

    def fetchall(self):
        return self.cur.fetchall()

    def fetchone(self):
        return self.cur.fetchone()

    def query(self, sql, params=None):
        self.cur.execute(sql, params or ())
        return self.fetchall()


