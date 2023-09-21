import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app import dp
from db.reports import get_reports_history
from utils import buttons, messages, states
import handlers.frequent_cases as fq
from dotenv import load_dotenv

load_dotenv()


@dp.message_handler(lambda m: m.text == buttons.search_btn.text)
async def search_command(message):
    await message.answer(messages.search_message(), reply_markup=buttons.back_to_menu_markup)
    await states.Search.is_active.set()


@dp.message_handler(state=states.Search.is_active)
async def handle_text(message, state):
    if message.text == buttons.back_to_menu_btn.text:
        await state.finish()
        return await fq.welcome_command(message)
    reports = get_reports_history()
    answer = f"Найденные совпадения по запросу {message.text}:\n"
    await message.answer(answer, reply_markup=buttons.back_to_menu_markup)
    for report in reports:
        doc = open(report[0], 'rb')
        res = messages.search_found(message.text.strip(), report)
        if res != '':
            kb = InlineKeyboardMarkup(resize_keyboard=True)
            await message.reply_document(document=doc, caption=res,
                                         reply_markup=kb.add(InlineKeyboardButton("Перейти в обсуждение",
                                                                                  url=os.getenv('CHANNEL_NAME') + str(
                                                                                      report[-1]))))
