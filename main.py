import asyncio
import aiogram
from config import dp
from handlers import (
    start,
)

start.register_start_handler(dp=dp)

if __name__ == '__main__':
    asyncio.start_polling(
        dp,
    )
