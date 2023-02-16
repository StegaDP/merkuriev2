from app import dp
from db import reports
from db.reports import get_reports_to_pay, save_payment
from utils import buttons, messages, channel_editor
from utils.user_approve import connection_approved, ConnectionMode


@dp.message_handler(lambda m: m.text == buttons.pay_btn.text)
async def pay_order_command(message):
    if not await connection_approved(ConnectionMode.pay, message):
        return
    not_payed = get_reports_to_pay()
    await message.answer(messages.count_of_founded_documents(len(not_payed)))
    for report in not_payed:
        doc = open(report[1], 'rb')
        await message.reply_document(document=doc, caption=messages.pay_message(report), reply_markup=buttons.pay_btn_2(report))


@dp.callback_query_handler(lambda d: "pay_" in d.data)
async def pay_order_btn_hndlr(data):
    if not await connection_approved(ConnectionMode.pay, data.message):
        return
    search_key = data.data.split('_')[1]
    save_payment(data['from']['id'], search_key)
    await channel_editor.edit_post(messages.history_message(reports.get_report_by_path(search_key)), search_key, buttons.none)
    await data.message.answer(messages.UPDATED)
