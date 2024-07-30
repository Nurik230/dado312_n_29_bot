from decouple import config
from aiogram import Dispatcher, Bot


token = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)