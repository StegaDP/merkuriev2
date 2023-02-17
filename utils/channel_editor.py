import os

from aiogram import types

from app import bot
from db import reports
from utils import buttons
channel_id = -1001742419815
channel_id = -1001615560336


async def create_post(new_text, new_document, report):
    message = await bot.send_document(channel_id, document=open(new_document, 'rb'), caption=new_text)
    print(message['message_id'])
    reports.save_message_id(message['message_id'], new_document)


async def edit_post(new_text, path, markup=''):
    await bot.edit_message_caption(chat_id=channel_id, message_id=reports.get_message_id(path)[0], caption=new_text)


async def edit_post_media(path, new_document):
    file_extension = os.path.splitext(new_document)[1]

    # Determine the media type based on the file extension
    if file_extension == ".jpg":
        media = types.InputMediaPhoto(media=open(new_document, 'rb'),
                                      caption=reports.get_report_by_id(new_document))
    elif file_extension == ".pdf":
        media = types.InputMediaDocument(media=open(new_document, 'rb'),
                                         caption=reports.get_report_by_id(new_document))
    await bot.edit_message_media(chat_id=channel_id, message_id=reports.get_message_id(new_document)[0],
                                 media=media)
    #await edit_post(reports.get_report_by_id(new_document) + "\n", new_document)

