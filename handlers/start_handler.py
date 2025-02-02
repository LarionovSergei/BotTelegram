import asyncio

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message()
async def command_start(message: Message):
    await message.answer(text="Реакция на команду старт")
    await message.answer_dice()


