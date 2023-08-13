from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Kategoriya').add('Savat').add('Aloqa')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Kategoriya').add('Savat').add('Aloqa').add('Admin')

admin_p = ReplyKeyboardMarkup(resize_keyboard=True)
admin_p.add("Mahsulot qo'sish").add("Mahsulot o'chirish").add('Other').add('Back')

catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(
    InlineKeyboardButton(text='Nike✔', callback_data='nike'),
    InlineKeyboardButton(text='Adidas👟', callback_data='adidas'),
    InlineKeyboardButton(text='Loro Piana👡', callback_data='loro-piana')
)
