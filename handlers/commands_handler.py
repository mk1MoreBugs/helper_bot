from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import dp, bot
from utils.generate_bot_help_message import generate_bot_help_message


@dp.message(CommandStart())
async def start_command(message: Message):
    welcome_message = (
        f"Привет, {message.from_user.first_name}!\n"
        f"Бот позволяет получить прогноз погоды или вывести случайную мотивирующую цитату.\n\n"
        f"Получить подробное описание комманд: /help\n"
        f"Вывести inline-меню: /inline_menu"
    )
    await message.answer(welcome_message)


@dp.message(Command("quote"))
async def quote_command(message: Message):
    await send_quote_using_chat_id(chat_id=message.chat.id)


async def send_quote_using_chat_id(chat_id: int):
    quote_message = "Тестовая цитата"
    await bot.send_message(chat_id=chat_id, text=quote_message)


@dp.message(Command("help"))
async def help_command(message: Message):
    help_message = await generate_bot_help_message()
    await message.answer(help_message)
