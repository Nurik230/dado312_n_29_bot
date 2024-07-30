from aiogram import types, Dispatcher
from config import bot


async def start_menu(message: types.Message):
    print(message)
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"привет {message.from_user.first_name}"
    )


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(
        start_menu,
        commands=['start']
    )
