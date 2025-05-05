from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    welcome_message = (
        f"Привет, {message.from_user.first_name}!\n"
        f"Бот позволяет получить прогноз погоды или вывести случайную мотивирующую цитату.\n\n"
        f"Получить подробное описание комманд: /help\n"
        f"Вывести inline-меню: /inline_menu"
    )
    await message.answer(welcome_message)
