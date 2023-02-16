from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup


create_new_order_btn = KeyboardButton("Создать новый счет")
approve_btn = KeyboardButton("Подтвердить счет")
pay_btn = KeyboardButton("Оплатить счет")
history_btn = KeyboardButton("История")
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(create_new_order_btn, approve_btn)
menu.add(pay_btn, history_btn)


show_all_posibilities_btn = KeyboardButton("Показать возможности каждого пользователя")
edit_posibilities_btn = KeyboardButton("Редактировать возможности пользователей")
back_to_menu_btn = KeyboardButton("Вернуться в меню")
back_to_menu_markup = ReplyKeyboardMarkup(resize_keyboard=True)
back_to_menu_markup.add(back_to_menu_btn)
admin_menu = ReplyKeyboardMarkup(resize_keyboard=True)
admin_menu.add(show_all_posibilities_btn)
admin_menu.add(edit_posibilities_btn)
admin_menu.add(back_to_menu_btn)

back_btn = KeyboardButton("Назад")


def users_btn(arr: list):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in arr:
        kb.add(KeyboardButton(f"{i[0]} (id: {i[1]})"))
    kb.add(back_btn)
    return kb


def get_posibilities_btns(t: tuple):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("[Можно создавать] сменить на [Нельзя создавать]"
                          if t[0] else "[Нельзя создавать] сменить на [Можно создавать]"))

    kb.add(KeyboardButton("[Можно согласовать] сменить на [Нельзя согласовать]"
                          if t[1] else "[Нельзя согласовать] сменить на [Можно согласовать]"))

    kb.add(KeyboardButton("[Можно оплатить] сменить на [Нельзя оплатить]"
                          if t[2] else "[Нельзя оплатить] сменить на [Можно оплатить]"))
    kb.add(back_btn)
    return kb


def approve_btn_2(report):
    kb = InlineKeyboardMarkup(resize_keyboard=True)
    kb.add(InlineKeyboardButton("Согласовать", callback_data=f"approve_{report[1]}"))
    return kb


def pay_btn_2(report):
    kb = InlineKeyboardMarkup(resize_keyboard=True)
    kb.add(InlineKeyboardButton("Оплатить", callback_data=f"pay_{report[1]}"))
    return kb
none = ReplyKeyboardRemove()
