from db.Postgres import Postgres


def add_new(user_id, path: str, description: str):
    sql = "INSERT into reports (created_by, document_name, description, creation_date)" \
          " values (%s, %s, %s, NOW())"
    with Postgres() as db_conn:
        db_conn.execute(sql, (user_id,
                              path,
                              description,))


def get_reports_to_approve():
    sql = "SELECT * FROM reports WHERE approve_date IS NULL"
    with Postgres() as db_conn:
        res = db_conn.query(sql, ())
    return res


def save_approvement(id, file_name):
    sql = "UPDATE reports SET approve_date=NOW(), approved_by=%s WHERE document_name=%s"
    with Postgres() as db_conn:
        db_conn.execute(sql, (id,file_name,))


def get_reports_to_pay():
    sql = "SELECT * FROM reports WHERE approve_date IS NOT NULL AND pay_date IS NULL"
    with Postgres() as db_conn:
        res = db_conn.query(sql, ())
    return res


def save_payment(id, file_name):
    sql = "UPDATE reports SET pay_date=NOW(), payed_by=%s WHERE document_name=%s"
    with Postgres() as db_conn:
        db_conn.execute(sql, (id,file_name,))


def get_reports_history():
    sql = "SELECT * FROM reports"
    with Postgres() as db_conn:
        res = db_conn.query(sql, ())
    return res


def get_report_by_path(path):
    sql = "SELECT * FROM reports WHERE document_name=%s"
    with Postgres() as db_conn:
        res = db_conn.query(sql, (path,))
    return res[0]


def get_message_id(path):
    print(path)
    sql = "SELECT message_id FROM reports WHERE document_name=%s"
    with Postgres() as db_conn:
        res = db_conn.query(sql, (path,))
    return res[0]


def get_report_by_id(path):
    sql = "SELECT description FROM reports WHERE document_name=%s"
    with Postgres() as db_conn:
        res = db_conn.query(sql, (path,))
    return res[0][0]
def save_message_id(message_id, path):
    sql = "UPDATE reports SET message_id=%s WHERE document_name=%s"
    with Postgres() as db_conn:
        db_conn.execute(sql, (message_id, path,))


def change_text(text, report):
    sql = "UPDATE reports SET description=%s WHERE document_name=%s"
    with Postgres() as db_conn:
        db_conn.execute(sql, (text, report,))


def change_attachment(src, report):
    sql = "UPDATE reports SET document_name=%s WHERE document_name=%s"
    with Postgres() as db_conn:
        db_conn.execute(sql, (src, report,))
