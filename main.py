import logging
import sys

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

# from app
from app import keyboards as kb
from app import database as db

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


async def on_startup(_):
    await db.db_start()
    print('Bot ishga tushdi!')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await db.cm_db_start(message.from_user.id)
    await message.answer_sticker(os.getenv('STICER_ID'))
    await message.answer(f'Assalomu aleykum {message.from_user.first_name}.\n'
                         f'Online krasovkalar do\'koniga xush kelibsiz!', reply_markup=kb.main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Siz Admin sifatida ro\'yxatdab o\'tdingiz!', reply_markup=kb.main_admin)


@dp.message_handler(text='Kategoriya')
async def kategoria(message: types.Message):
    await message.answer(f'Siz kategroiadasiz!', reply_markup=kb.catalog_list)


@dp.message_handler(text='Savat')
async def savat(message: types.Message):
    await message.answer(f'Siz Savatdasiz!')


@dp.message_handler(text='Aloqa')
async def aloqa(message: types.Message):
    await message.answer(f'Siz Aloqadasiz!')


@dp.message_handler(text='Admin')
async def admin_panel(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Admin panelga kirdingiz!', reply_markup=kb.admin_p)
    else:
        await message.reply('Sizni tushunmayabman!')


@dp.message_handler(text='Back')
async def admin_panel(message: types.Message):
    await message.answer('Orqaga qaytdingiz!', reply_markup=kb.main_admin)


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Sizni tushunmayabman!')


@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == 'nike':
        await bot.send_message(chat_id=callback_query.from_user.id, text='Siz Nike brandini tanladingiz!')
    elif callback_query.data == 'adidas':
        await bot.send_message(chat_id=callback_query.from_user.id, text='Siz Adidas brandini tanladingiz!')
    elif callback_query.data == 'loro-piana':
        await bot.send_message(chat_id=callback_query.from_user.id, text='Siz Loro Piana brandini tanladingiz!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
