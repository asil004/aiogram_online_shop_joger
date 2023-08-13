import logging
import sys

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMhZNjD8pqUKrYugcA5mGEoWtpDZVMAAiUAA7KYmg4PNnd8jpPBLTAE')
    await message.answer(f'Assalomu aleykum {message.from_user.first_name}.\n'
                         f'Online krasovkalar do\'koniga xush kelibsiz!')


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Sizni tushunmayabman!')


@dp.message_handler(content_types=['sticker'])
async def sticker(message: types.Message):
    await message.reply(message.sticker.file_id)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        executor.start_polling(dp)
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
