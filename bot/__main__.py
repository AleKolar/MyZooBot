import asyncio
import logging


from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot.config import token
from bot.flask import keep_alive
from handlers.try_choosing_handlers import router

__all__ = ['router']

logging.basicConfig(level=logging.INFO)

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(token)
#bot = Bot(os.getenv('token'))


async def main():
    #bot = Bot(os.getenv('token'))
    bot = Bot(token)
    dp = Dispatcher()

    dp.include_routers(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

keep_alive()
if __name__ == "__main__":
    asyncio.run(main())