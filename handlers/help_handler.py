from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from utils.generate_bot_help_message import generate_bot_help_message

router = Router()


@router.message(Command("help"))
async def help_command(message: Message):
    help_message = await generate_bot_help_message()
    await message.answer(help_message)
