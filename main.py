import config
from aiogram import Bot, Dispatcher, types, F
import logging
import asyncio
from handlers import common, get_weather

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.token)
    dp = Dispatcher()
    dp.include_router(get_weather.router)
    dp.include_router(common.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
