from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def command_start(message: Message, db):
    await message.answer(text="Реакция на команду старт")
    await message.answer_dice()


