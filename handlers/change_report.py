from app import dp, bot
from db.reports import get_reports_to_approve, change_text, change_attachment
from handlers.create_order import get_random_name
from utils import buttons, messages
from utils.channel_editor import edit_post, edit_post_media
from utils.messages import UPDATED
from utils.states import ChangeReport
from utils.user_approve import connection_approved, ConnectionMode
import handlers.frequent_cases as fq


async def write_file(message):
    file_info = await bot.get_file(message.document.file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    src = 'db/files/' + await get_random_name() + "." + file_info.file_path.split('.')[-1]
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file.read())
    return src


@dp.message_handler(lambda m: m.text == buttons.change_report_btn.text)
async def approve_order_command(message):
    if not await connection_approved(ConnectionMode.approve, message):
        return
    not_approved = get_reports_to_approve()
    await message.answer(messages.count_of_founded_documents(len(not_approved)))
    for report in not_approved:
        doc = open(report[1], 'rb')
        await message.reply_document(document=doc, caption=messages.approve_message(report),
                                     reply_markup=buttons.change_report_btn_2(report))


@dp.callback_query_handler(lambda d: 'change_text_' in d.data)
async def change_text_command(data, state):
    print("yR")
    await data.message.answer("Введите новый текст:", reply_markup=buttons.back_to_menu_markup)
    await ChangeReport.text.set()
    async with state.proxy() as d:
        d["start"] = data.data.split('_')[2]
    await ChangeReport.text.set()

@dp.callback_query_handler(lambda d: 'change_attachment_' in d.data)
async def change_attachment_command(data, state):
    async with state.proxy() as d:
        d["start"] = data.data.split('_')[2]
    await data.message.answer("Отправьте новое вложение:", reply_markup=buttons.back_to_menu_markup)
    await ChangeReport.attachment.set()


@dp.message_handler(state=ChangeReport.text)
async def change_text_command_2(message, state):
    if message.text == buttons.back_to_menu_btn.text:
        await state.finish()
        return await fq.welcome_command(message)

    if 'text' not in dict(message).keys():
        await message.answer(messages.INCORRECT_MESSAGE)
        return
    async with state.proxy() as data:
        information = data.as_dict()
    change_text(message.text, information['start'])
    await edit_post(message.text, information['start'])
    await state.finish()
    await message.answer(UPDATED)
    return await fq.welcome_command(message)


@dp.message_handler(state=ChangeReport.attachment, content_types=['document', 'photo', 'text'])
async def change_attachment_command_2(message, state):
    if message.text == buttons.back_to_menu_btn.text:
        await state.finish()
        return await fq.welcome_command(message)
    src = None
    if 'photo' in dict(message).keys():
        filename = 'db/files/' + await get_random_name() + '.jpg'
        await message.photo[-1].download(filename)
        src = filename

    if 'document' in dict(message).keys():
        src = await write_file(message)
    if not src:
        await message.answer(messages.INCORRECT_MESSAGE)
        return
    async with state.proxy() as data:
        information = data.as_dict()
    change_attachment(src, information['start'])
    await edit_post_media(information['start'], src)
    await state.finish()
    await message.answer(UPDATED)
    return await fq.welcome_command(message)
