from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def start(message: Message):
	user_id = message.from_user.id
	await message.answer(f"Твой id {user_id}")

