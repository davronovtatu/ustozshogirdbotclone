from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text=f"Assalom alaykum {message.from_user.full_name}\n"
    text+=f"UstozShogird kanalining rasmiy botiga xush kelibsiz!\n"
    text+=f"/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!\n"

    await message.answer(text,reply_markup=menu)


