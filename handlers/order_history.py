from app import dp
from utils import buttons, messages
from db.reports import get_reports_history


@dp.message_handler(lambda m: m.text == buttons.history_btn.text)
async def history(message):
    reports = get_reports_history()
    await message.answer(messages.count_of_founded_documents(len(reports)))
    for report in reports:
        doc = open(report[1], 'rb')
        await message.reply_document(document=doc, caption=messages.history_message(report))
