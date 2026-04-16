from aiogram.fileters import Command

import asyncio
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import CommandStart

TOKEN = "8333349750:AAFpxCIU3z5ly__Y1AhK1Dkg2f1wC7W5rCM"

bot = Bot(token=TOKEN)
dp = Dispatcher()


# 👇 ШУТКИ
jokes = [
    "Я бы ответил умно, но у меня нет лицензии на интеллект 🤖",
    "Секунду… я думаю… ой, всё 💀",
    "Ошибка 404: смысл не найден",
    "Я бот, но даже я не понял это сообщение 😄",
    "Ты это сейчас серьёзно написал? 👀",
    "Мой процессор сказал: «я устал» 💤",
    "Я пытался понять… честно… не получилось 🫠",
    "Это сообщение отправлено в параллельную вселенную 🌌",
    "Я завис… но красиво ✨",
    "Слишком сложно для моего железа 🧠",
    "Я это прочитал и теперь мне нужно лечь 🤖",
    "Ты пишешь или случайно клавиатуру чистишь? 😄",
]

@dp.message()
async def test_all(message: Message):
    await message.answer("ТЕСТ РАБОТАЕТ")

# 👇 /start
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать в магазин VexoShop!\n\n"
        "📨 Связь: @livaxw\n\n"
        "Пока наш сайт еще не создан, наш товар можно купить написав нашему менеджеру више",
            )

# 👇 РАНДОМ ОТВЕТЫ НА ВСЕ СООБЩЕНИЯ
@dp.message(F.text)
async def random_reply(message: types.Message):
    if message.text.startswith("/"):
        return

    await message.answer(random.choice(jokes))

# 👇 запуск
async def main():
    print("Bot Started ✅")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

