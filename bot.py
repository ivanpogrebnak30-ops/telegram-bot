import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

bot = Bot(token="8333349750:AAFpxCIU3z5ly__Y1AhK1Dkg2f1wC7W5rCM")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Бот работает 24/7!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
