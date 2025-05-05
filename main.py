import asyncio
import logging
import sys

from aiogram.types import BotCommand

from config import bot, dp, job_scheduler
from handlers import subscribe_handler
from handlers import inline_menu_handler
from handlers import weather_handler
from handlers import start_handler
from handlers import help_handler
from handlers import quote_handler


async def main() -> None:
    job_scheduler.start()

    bot_commands = [
        BotCommand(command='start', description='Приветствие'),
        BotCommand(command='weather', description='Текущая погода в городе'), #<город>
        BotCommand(command='quote', description='Случайная мотивирующая цитата'),
        BotCommand(command='subscribe', description='Подписка на ежедневную погоду и цитату'),
        BotCommand(command='help', description='Список команд'),
        BotCommand(command='inline_menu', description='Вызвать меню'),
    ]
    await bot.set_my_commands(bot_commands)

    dp.include_router(start_handler.router)
    dp.include_router(help_handler.router)
    dp.include_router(inline_menu_handler.router)
    dp.include_router(weather_handler.router)
    dp.include_router(quote_handler.router)
    dp.include_router(subscribe_handler.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
