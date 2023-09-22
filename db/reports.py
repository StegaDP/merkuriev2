import sqlite3


def add_new(user_id, path: str, description: str):
    sql = "INSERT INTO reports (created_by, document_name, description, creation_date) VALUES (?, ?, ?, datetime('now'))"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (user_id, path, description))


def get_reports_to_approve():
    sql = "SELECT * FROM reports WHERE approve_date IS NULL"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def save_approvement(id, file_name):
    sql = "UPDATE reports SET approve_date=datetime('now'), approved_by=? WHERE document_name=?"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (id, file_name))


def get_reports_to_pay():
    sql = "SELECT * FROM reports WHERE approve_date IS NOT NULL AND pay_date IS NULL"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def save_payment(id, file_name):
    sql = "UPDATE reports SET pay_date=datetime('now'), payed_by=? WHERE document_name=?"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (id, file_name))


def get_reports_history():
    sql = "SELECT * FROM reports"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def get_report_by_path(path):
    sql = "SELECT * FROM reports WHERE document_name=?"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (path,))
        result = cursor.fetchone()
    return result


def get_message_id(path):
    sql = "SELECT message_id FROM reports WHERE document_name=?"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (path,))
        result = cursor.fetchone()
    return result


def get_report_by_id(path):
    sql = "SELECT description FROM reports WHERE document_name=?"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (path,))
        result = cursor.fetchone()
    return result[0]


def save_message_id(message_id, path):
    sql = "UPDATE reports SET message_id=? WHERE document_name=?"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (message_id, path))


def change_text(text, report):
    sql = "UPDATE reports SET description=? WHERE document_name=?"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (text, report))


def change_attachment(src, report):
    sql = "UPDATE reports SET document_name=? WHERE document_name=?"
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (src, report))