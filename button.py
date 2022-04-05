from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(row_width=2)
rick = InlineKeyboardButton(text='🧠Rick Sanchez', callback_data='Rick Sanchez')
morty = InlineKeyboardButton(text='👦Morty Smith', callback_data='Morty Smith')
summer = InlineKeyboardButton(text='👩🏻‍🦰Summer Smith', callback_data='Summer Smith')
jerry = InlineKeyboardButton(text='👨🏻Jerry Smith',callback_data='Jerry Smith')
beth = InlineKeyboardButton(text='👩🏼Beth Smith',callback_data='Beth Smith')
squanchy = InlineKeyboardButton(text='🦊Squancy',callback_data='Squanchy')
kromb = InlineKeyboardButton(text='🪰Krombopulos Michael',callback_data='Krombopulos Michael')
giraffe = InlineKeyboardButton(text='🦒Reverse Giraffe', callback_data='Reverse Giraffe')
birdperson = InlineKeyboardButton(text='🐦Birdperson',callback_data='Birdperson')

main_menu.insert(rick)
main_menu.insert(morty)
main_menu.insert(summer)
main_menu.insert(jerry)
main_menu.insert(beth)
main_menu.insert(squanchy)
main_menu.insert(kromb)
main_menu.insert(giraffe)
main_menu.insert(birdperson)


