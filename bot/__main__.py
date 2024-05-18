import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import token
from try_choosing_handlers import router

__all__ = ['router']

logging.basicConfig(level=logging.INFO)

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(token)


async def main():
    #bot = Bot(os.getenv('token'))
    bot = Bot(token)
    dp = Dispatcher()

    dp.include_routers(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())