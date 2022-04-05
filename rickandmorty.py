

import logging
from aiogram import Bot, Dispatcher, executor, types
from character import main as choose_character
from button import main_menu
from aiogram.types import ParseMode
from aiogram.utils.markdown import text, bold


token_rm = ''

logging.basicConfig(level=logging.INFO)


bot = Bot(token=token_rm)
dp = Dispatcher(bot)



@dp.message_handler(commands= ['start'])
async def send(message: types.Message):
    msg = text(bold("Привет🖐 \nДобро пожаловать в мир Rick and Morty \nВыбери персонажа"))
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu)



@dp.callback_query_handler(text = 'Rick Sanchez')
async def rick(callback: types.CallbackQuery):
    await callback.message.answer(choose_character('Rick Sanchez'))

@dp.callback_query_handler(text = 'Morty Smith')
async def rick(callback: types.CallbackQuery):
    await callback.message.answer(choose_character('Morty Smith'))

@dp.callback_query_handler(text = 'Summer Smith')
async def rick(callback: types.CallbackQuery):
    await callback.message.answer(choose_character('Summer Smith'))

@dp.callback_query_handler(text = 'Jerry Smith')
async def rick(callback: types.CallbackQuery):
    await callback.message.answer(choose_character('Jerry Smith'))

@dp.callback_query_handler(text = 'Beth Smith')
async def rick(callback: types.CallbackQuery):
    await callback.message.answer(choose_character('Beth Smith'))

@dp.callback_query_handler(text = 'Squanchy')
async def rick(callback: types.CallbackQuery):
    await callback.message.answer(choose_character('Squanchy'))

@dp.callback_query_handler(text= 'Krombopulos Michael')
async def rick(callback: types.CallbackQuery):
    await callback.message.answer(choose_character('Krombopulos Michael'))

@dp.callback_query_handler(text = 'Reverse Giraffe')
async def rick(callback: types.CallbackQuery):
    await callback.message.answer(choose_character('Reverse Giraffe'))

@dp.callback_query_handler(text = 'Birdperson')
async def rick(callback: types.CallbackQuery):
    await callback.message.answer(choose_character('Birdperson'))


if __name__ == '__main__':
    executor.start_polling(dp)


