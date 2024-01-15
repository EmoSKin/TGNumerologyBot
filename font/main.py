# main.py
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types
from config import API_TOKEN
import handlers

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

handlers.setup(dp)

async def send_start_keyboard(message: types.Message) -> None:
    await handlers.start_keyboard(message)

async def main() -> None:
    dp.register_message_handler(send_start_keyboard, commands=['start'])

    await dp.start_polling()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())