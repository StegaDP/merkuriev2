import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TELEGRAM_API_TOKEN = '5389632951:AAE-eYPqbHMrszD9afgtaxC6b9lbpNrWaZ0'
ADMIN_LIST = [1398715343,229855438]
CHANNEL_NAME = 'https://t.me/odpashtest/'


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)
