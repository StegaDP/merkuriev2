import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app import dp
from utils import buttons, messages
from db.reports import get_reports_history
from dotenv import load_dotenv

load_dotenv()


@dp.message_handler(lambda m: m.text == buttons.history_btn.text)
async def history(message):
    reports = get_reports_history()
    await message.answer(messages.count_of_founded_documents(len(reports)))
    for report in reports:
        doc = open(report[1], 'rb')
        kb = InlineKeyboardMarkup(resize_keyboard=True)
        await message.reply_document(document=doc, caption=messages.history_message(report),
                                     reply_markup=kb.add(InlineKeyboardButton("Перейти в обсуждение",
                                                                              url=os.getenv('CHANNEL_NAME') + str(
                                                                                  report[-1]))))
