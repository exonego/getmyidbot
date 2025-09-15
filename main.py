from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from environs import Env

env = Env()
env.read_env()

bot = Bot(token=env("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text="Привет! Я отправляю твой user_id!")
    await message.answer(text=str(message.from_user.id))


@dp.message()
async def process_any_message(message: Message):
    await message.answer(text=str(message.from_user.id))


if __name__ == "__main__":
    dp.run_polling(bot)
