import logging
import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
import json


load_dotenv(".env")
logging.basicConfig(level=logging.INFO)
ADMIN_LIST = json.loads(os.environ.get("ADMIN_LIST"))
bot = Bot(token=os.environ.get("TELEGRAM_API_TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

if __name__ == "__main__":
    from handlers import dp

    executor.start_polling(dp, skip_updates=True)
