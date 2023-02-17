from db.reports import get_reports_history
from db.user import get_all_user_information, u_info

START_MESSAGE = "Добро пожаловать в бот!"
NOT_ADMIN = "Вы не состоите в базе админов!"
ADMIN_MENU = "Добро пожаловать в Админку!\nВыберите действие:"
EDIT_POSIBILITIES = "Выберите аккаунт:"
UPDATED = "Изменения учтены!"
ERROR = "Ошибка!"
INCORRECT_MESSAGE = "Неправильный ввод!\nОтправьте файл или фото:"
SEND_DOCUMENT = "Отправьте фото или документ:"
WRITE_DESCRIPTION = "Напишите описание:"
SHOW_ID_TEXT = "Показать ID"
SERVER_ERROR = "Ошибка сервера!"
NOT_APPROVED = "У вас нет прав для просмотра данного раздела!"


def SHOW_ID(id: int):
    return f"Ваш ID: {id}\nПерешлите его админу"


def get_all_posibilities():
    information = get_all_user_information()
    message = ""
    for i in information:
        can_pay = '+' if i[3] else '-'
        can_approve = '+' if i[2] else '-'
        can_create = '+' if i[1] else '-'
        message += f"Пользователь: {i[4]} ({i[0]})\nМожет платить: {can_pay}\nМожет согласовывать: " \
                   f"{can_approve}\nМожет создавать: {can_create}\n\n"
    return message


def approve_message(report):
    message = f"⚪Создано пользователем: {u_info(report[0])[4]}\nОписание: {report[2]}\nДата создания: {str(report[3]).split('.')[0]}\n----------------------------\n"
    return message


def pay_message(report):
    if report[4] is None:
        return approve_message(report)
    message = approve_message(
        report) + f"\n🟡️Согласовано пользователем: {u_info(report[6])[4]}\nДата согласования: {str(report[4]).split('.')[0]}\n----------------------------\n"
    return message


def count_of_founded_documents(count):
    return f"Найдено {count} документов!"


def search_message():
    return "Для поиска введите запрос (поиск доступен по полям, сумме и описанию):"


def search_found(text, report):
    m = history_message(report)
    if text.lower() in m.lower():
        return m
    return ''

def history_message(report):
    message = pay_message(report)
    if report[5] is None:
        return message
    print(report)
    return message + f"\n🟢Оплчено пользователем: {u_info(report[7])[4]}\nДата оплаты: {str(report[5]).split('.')[0]}"
