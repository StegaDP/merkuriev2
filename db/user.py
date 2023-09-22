import sqlite3


def user_not_in_db(id: int) -> bool:
    sql = "SELECT * FROM users WHERE id = ?"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        result = cursor.fetchall()
    if len(result) == 0:
        return False
    return True


def add_new_user(id: int, name: str):
    sql = "INSERT INTO users VALUES (?, ?, ?, ?, ?)"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (id, False, False, False, name))


def show_all_users() -> list:
    sql = "SELECT name, id FROM users"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def get_user_posibilities(id: int) -> tuple:
    sql = "SELECT can_create, can_approve, can_pay FROM users WHERE id=?"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        result = cursor.fetchall()
    return result[0]


def update_mode(id: int, mode: str, to_set: bool):
    if mode == 'can_create':
        sql = "UPDATE users SET can_create=? WHERE id=?"
    elif mode == 'can_approve':
        sql = "UPDATE users SET can_approve=? WHERE id=?"
    elif mode == 'can_pay':
        sql = "UPDATE users SET can_pay=? WHERE id=?"
    else:
        sql = ''
    if sql != '':
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (to_set, id))


def get_all_user_information():
    sql = "SELECT * FROM users"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def u_info(id: int):
    sql = "SELECT * FROM users WHERE id=?"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        result = cursor.fetchall()
    return result[0]