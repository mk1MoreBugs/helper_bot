from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import bot

router = Router()


@router.message(Command("quote"))
async def quote_command(message: Message):
    await send_quote_using_chat_id(chat_id=message.chat.id)


async def send_quote_using_chat_id(chat_id: int):
    quote_message = "Тестовая цитата"
    await bot.send_message(chat_id=chat_id, text=quote_message)
