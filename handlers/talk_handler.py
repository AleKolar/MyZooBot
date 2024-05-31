from datetime import datetime

from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message

router = Router()
@router.message()
async def talk_with_me(message: Message):
    time_now = datetime.now().strftime('%H:%M')
    added_text = (f"Создано в {time_now}")
    await message.answer(f"{added_text}\n\n{"Я здесь не для общения, а чтоб определить Вашего Питомца"}", parse_mode=ParseMode.MARKDOWN_V2)