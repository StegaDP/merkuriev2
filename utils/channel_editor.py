from app import bot
from db import reports
from utils import buttons
channel_id = -1001742419815
channel_id = -1001615560336


async def create_post(new_text, new_document, report):
    message = await bot.send_document(channel_id, document=open(new_document, 'rb'), caption=new_text)
    print(message['message_id'])
    reports.save_message_id(message['message_id'], new_document)


async def edit_post(new_text, path, markup):
    await bot.edit_message_caption(chat_id=channel_id, message_id=reports.get_message_id(path)[0], caption=new_text)


