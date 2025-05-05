from aiogram.types import BotCommand

from config import bot


async def generate_bot_help_message() -> str:
    bot_commands: list[BotCommand] = await bot.get_my_commands()

    help_message = ""

    for command in bot_commands:
        help_message += f"/{command.command} - {command.description} \n\n"

    help_message = help_message.replace("/weather", "/weather Город")

    return help_message
