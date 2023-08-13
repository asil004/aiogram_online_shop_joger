import logging
import sys

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(f'Assalomu aleykum {message.from_user.first_name}.\n'
                         f'Online krasovkalar do\'koniga xush kelibsiz!')


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Sizni tushunmayabman!------')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        executor.start_polling(dp)
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
