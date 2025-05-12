from aiogram.types import BotCommand

from config import bot


async def generate_bot_help_message() -> str:
    bot_commands: list[BotCommand] = await bot.get_my_commands()

    help_message = ""

    for command in bot_commands:
        help_message += f"/{command.command} - {command.description} \n\n"

    help_message = help_message.replace("/weather", "/weather Город")

    help_message += (
        "\n"
        "Команда /weather использует OpenWeatherMap API https://openweathermap.org/api\n"
        "Команда /quote использует GigaChat API https://developers.sber.ru/portal/products/gigachat-api"
    )

    return help_message
