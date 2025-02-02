import asyncio
import logging

from aiogram import Bot, Dispatcher
import config
from handlers.start_handler import router


async def main():
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
