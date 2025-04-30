import asyncio
import logging
import sys

from aiogram.types import BotCommand

from dispatcher import bot, dp
import handlers.commands_handler  # handlers should be placed before run the main() function


async def main() -> None:

    bot_commands = [
        BotCommand(command='start', description='Приветствие'),
        BotCommand(command='weather', description='Текущая погода в городе'), #<город>
        BotCommand(command='quote', description='Случайная мотивирующая цитата'),
        BotCommand(command='subscribe', description='Подписка на ежедневную погоду и цитату'),
        BotCommand(command='help', description='Список команд'),
        BotCommand(command='inline_menu', description='Вызвать меню'),
    ]
    await bot.set_my_commands(bot_commands)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
