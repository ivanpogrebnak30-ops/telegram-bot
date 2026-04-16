import asyncio
import random
import logging
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import CommandStart

# 🔧 логирование (чтобы видеть ошибки в Render)
logging.basicConfig(level=logging.INFO)

# 🔑 токен (ОБЯЗАТЕЛЬНО через Render Environment)
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# 🌐 КНОПКА САЙТА (ВСТАВЬ СВОЮ ССЫЛКУ)
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=" Открыть сайт", web_app=WebAppInfo(url="https://gaze-yielding-firefly.tilda.ws/"))]
    ],
    resize_keyboard=True
)


# 😂 ШУТКИ
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
    "Это сейчас был запрос или заклинание? 🧙‍♂️",
    "Я пытался перевести… Google сдался 😶",
    "Слишком мощно, я не вывожу 😵"
]


# 🚀 /start (ТВОЁ ПРИВЕТСТВИЕ)
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать в магазин VexoShop!\n\n"
        "📨 Связь: @livaxw\n\n"
        "🤷‍♂️ Пока наш сайт еще не создан, наш товар можно купить написав нашему менеджеру выше",
        reply_markup=kb
    )


# 💬 ОСНОВНАЯ ЛОГИКА (умные + смешные ответы)
@dp.message(F.text)
async def chat(message: types.Message):
    text = message.text.lower()

    # игнор команд
    
