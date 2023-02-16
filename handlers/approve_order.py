from app import dp
from db import reports
from utils.user_approve import connection_approved, ConnectionMode
from db.reports import get_reports_to_approve, save_approvement
from utils import messages, buttons, channel_editor


@dp.message_handler(lambda m: m.text == buttons.approve_btn.text)
async def approve_order_command(message):
    if not await connection_approved(ConnectionMode.approve, message):
        return
    not_approved = get_reports_to_approve()
    await message.answer(messages.count_of_founded_documents(len(not_approved)))
    for report in not_approved:
        doc = open(report[1], 'rb')
        await message.reply_document(document=doc, caption=messages.approve_message(report), reply_markup=buttons.approve_btn_2(report))


@dp.callback_query_handler(lambda d: "approve_" in d.data)
async def approve_order_btn_hndlr(data):
    if not await connection_approved(ConnectionMode.approve, data.message):
        return
    search_key = data.data.split('_')[1]
    save_approvement(data['from']['id'], search_key)
    report = reports.get_report_by_path(search_key)
    await channel_editor.edit_post(messages.pay_message(reports.get_report_by_path(search_key)), search_key, buttons.pay_btn_2(report))
    await data.message.answer(messages.UPDATED)
