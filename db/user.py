from db.Postgres import Postgres


def user_not_in_db(id: int) -> bool:
    sql = "SELECT * FROM users WHERE id = %s"
    with Postgres() as db_conn:
        result = db_conn.query(sql, (id,))
    if len(result) == 0:
        return False
    return True


def add_new_user(id: int, name: str):
    sql = "INSERT into users values (%s, %s, %s, %s, %s)"
    with Postgres() as db_conn:
        db_conn.execute(sql, (id, False, False, False, name,))


def show_all_users() -> list:
    sql = "SELECT name, id FROM users"
    with Postgres() as db_conn:
        result = db_conn.query(sql)
    return result


def get_user_posibilities(id: int) -> tuple:
    sql = "SELECT can_create, can_approve, can_pay FROM users WHERE id=%s"
    with Postgres() as db_conn:
        result = db_conn.query(sql, (id,))
    return result[0]


def update_mode(id: int, mode: str, to_set: bool):
    if mode == 'can_create':
        sql = "UPDATE users SET can_create=%s WHERE id=%s"
    elif mode == 'can_approve':
        sql = "UPDATE users SET can_approve=%s WHERE id=%s"
    elif mode == 'can_pay':
        sql = "UPDATE users SET can_pay=%s WHERE id=%s"
    else:
        sql = ''
    if sql != '':
        with Postgres() as db_conn:
            db_conn.execute(sql, (to_set, id,))


def get_all_user_information():
    sql = "SELECT * FROM users"
    with Postgres() as db_conn:
        result = db_conn.query(sql)
    return result


def u_info(id: int):
    sql = f"SELECT * FROM users WHERE id=%s"
    with Postgres() as db_conn:
        result = db_conn.query(sql, (id,))
    return result[0]
