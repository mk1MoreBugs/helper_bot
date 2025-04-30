from aiogram.types import Message

def parse_city_arg(message: Message) -> str:
    message_as_list = message.text.split()
    message_as_list.pop(0)
    return " ".join(message_as_list)
