from aiogram import types

from db.user import user_not_in_db, add_new_user
from utils import messages, channel_editor
from utils import buttons
from app import dp


@dp.message_handler(commands=["start", "help"])
async def welcome_command(message: types.Message):
    print(message)

    #await channel_editor.create_post(message, "lalal", "")
    if not user_not_in_db(message.chat.id):

        add_new_user(message.chat.id, f"{message.chat.first_name} {message.chat.last_name}")

    await message.reply(
        messages.START_MESSAGE,
        reply_markup=buttons.menu,
    )


@dp.message_handler(lambda m: m.text == messages.SHOW_ID_TEXT)
async def show_id_command(message: types.Message):
    await message.reply(messages.SHOW_ID(message.chat.id), reply_markup=buttons.menu)


@dp.message_handler(lambda m: m.text == buttons.back_to_menu_btn.text)
async def back_to_menu_command(message: types.Message):
    await welcome_command(message)
