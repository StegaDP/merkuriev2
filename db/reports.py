from db.Postgres import SQLite

conn = SQLite().conn
cur = conn.cursor()


def add_new(user_id, path: str, description: str):
    sql = "INSERT into reports (created_by, document_name, description, creation_date)" \
          " values (?, ?, ?, datetime('now'))"
    cur.execute(sql, (user_id, path, description))
    conn.commit()


def get_reports_to_approve():
    sql = "SELECT * FROM reports WHERE approve_date IS NULL"
    cur.execute(sql)
    res = cur.fetchall()
    return res


def save_approvement(id, file_name):
    sql = "UPDATE reports SET approve_date=datetime('now'), approved_by=? WHERE document_name=?"
    cur.execute(sql, (id, file_name))
    conn.commit()


def get_reports_to_pay():
    sql = "SELECT * FROM reports WHERE approve_date IS NOT NULL AND pay_date IS NULL"
    cur.execute(sql)
    res = cur.fetchall()
    return res


def save_payment(id, file_name):
    sql = "UPDATE reports SET pay_date=datetime('now'), payed_by=? WHERE document_name=?"
    cur.execute(sql, (id, file_name))
    conn.commit()


def get_reports_history():
    sql = "SELECT * FROM reports"
    cur.execute(sql)
    res = cur.fetchall()
    return res


def get_report_by_path(path):
    sql = "SELECT * FROM reports WHERE document_name=?"
    cur.execute(sql, (path,))
    res = cur.fetchone()
    return res


def get_message_id(path):
    sql = "SELECT * FROM reports WHERE document_name=?"
    cur.execute(sql, (path,))
    res = cur.fetchone()
    return res


def get_report_by_id(path):
    sql = "SELECT description FROM reports WHERE document_name=?"
    cur.execute(sql, (path,))
    res = cur.fetchone()
    return res

def save_message_id(message_id, path):
    sql = "UPDATE reports SET message_id=? WHERE document_name=?"
    cur.execute(sql, (message_id, path))
    conn.commit()

def change_text(text, report):
    sql = "UPDATE reports SET description=? WHERE document_name=?"
    cur.execute(sql, (text, report))
    conn.commit()


def change_attachment(src, report):
    sql = "UPDATE reports SET document_name=? WHERE document_name=?"
    cur.execute(sql, (src, report))
    conn.commit()
