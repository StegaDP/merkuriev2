from aiogram import types
from aiogram.dispatcher import FSMContext

from app import dp, ADMIN_LIST
from db.user import show_all_users, get_user_posibilities, update_mode
from utils import messages, buttons
from utils.states import Admin


@dp.message_handler(commands=["admin"])
async def admin_command(message: types.Message):
    if message.from_user.id not in ADMIN_LIST:
        await message.reply(messages.NOT_ADMIN)
    else:
        await message.reply(messages.ADMIN_MENU, reply_markup=buttons.admin_menu)


@dp.message_handler(lambda m: m.text == buttons.show_all_posibilities_btn.text)
async def show_all_posibilities_command(message: types.Message):
    await message.answer(messages.get_all_posibilities(), reply_markup=buttons.admin_menu)


@dp.message_handler(lambda m: m.text == buttons.edit_posibilities_btn.text)
async def edit_posibilities_command(message: types.Message):
    await message.reply(messages.EDIT_POSIBILITIES, reply_markup=buttons.users_btn(show_all_users()))
    await Admin.edit.set()


@dp.message_handler(state=Admin.edit)
async def edit_posibilities_user_command(message: types.Message, state: FSMContext):
    if message.text == buttons.back_btn.text:
        await state.finish()
        await admin_command(message)
        return
    if 'сменить на' in message.text:
        if 'создавать' in message.text:
            mode = 'can_create'
        elif 'согласовать' in message.text:
            mode = 'can_approve'
        elif 'оплатить':
            mode = 'can_pay'
        else:
            mode = ''

        if mode != '':
            to_set = False if message.text.index("Можно") < message.text.index("Нельзя") else True

            async with state.proxy() as data:
                information = data.as_dict()
            update_mode(information['edit'], mode, to_set)
            await message.answer(messages.UPDATED)
        else:
            await message.answer(messages.ERROR)
    else:
        async with state.proxy() as data:
            data["edit"] = int(message.text.split('(')[1].replace(')', '').replace("'", '').replace('id: ', ''))

    async with state.proxy() as data:
        information = data.as_dict()
    await message.answer(f"Для изменения параметра нажмите на кнопку:", reply_markup=buttons.get_posibilities_btns(get_user_posibilities(information['edit'])))
