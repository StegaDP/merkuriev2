from db.Postgres import SQLite
import sqlite3

conn = SQLite().conn
cur = conn.cursor()

def user_not_in_db(id: int) -> bool:
    sql = "SELECT * FROM users WHERE id = ?"
    cur.execute(sql, (id,))
    result = cur.fetchall()
    if len(result) == 0:
        return False
    return True


def add_new_user(id: int, name: str):
    sql = "INSERT INTO users VALUES (?, ?, ?, ?, ?)"
    cur.execute(sql, (id, False, False, False, name,))
    conn.commit()


def show_all_users() -> list:
    sql = "SELECT name, id FROM users"
    cur.execute(sql)
    result = cur.fetchall()
    return result


def get_user_posibilities(id: int) -> tuple:
    sql = "SELECT can_create, can_approve, can_pay FROM users WHERE id=?"
    cur.execute(sql, (id,))
    result = cur.fetchone()
    return result


def update_mode(id: int, mode: str, to_set: bool):
    if mode == 'can_create':
        sql = "UPDATE users SET can_create=? WHERE id=?"
    elif mode == 'can_approve':
        sql = "UPDATE users SET can_approve=? WHERE id=?"
    elif mode == 'can_pay':
        sql = "UPDATE users SET can_pay=? WHERE id=?"
    else:
        return
    cur.execute(sql, (to_set, id))
    conn.commit()


def get_all_user_information():
    sql = "SELECT * FROM users"
    cur.execute(sql)
    result = cur.fetchall()
    return result


def u_info(id: int):
    sql = "SELECT * FROM users WHERE id=?"
    cur.execute(sql, (id,))
    result = cur.fetchone()
    return result
