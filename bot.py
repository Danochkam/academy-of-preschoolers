"""Academy of Preschoolers: a Russian-language Telegram course information bot.

Configuration is loaded from a local .env file or environment variables.
Never publish the .env file or your Telegram bot token.
"""

import asyncio
import logging
import os
from pathlib import Path

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery,
    FSInputFile,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
MANAGER_URL = os.getenv("MANAGER_WHATSAPP_URL", "").strip()
PAYMENT_INSTRUCTIONS = os.getenv("PAYMENT_INSTRUCTIONS", "").replace("\\n", "\n").strip()
VIDEO_PATH = Path(__file__).parent / "video.mp4"

dp = Dispatcher()


def course_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="📹 Посмотреть пример урока", callback_data="video")],
        [InlineKeyboardButton(text="💰 Узнать стоимость", callback_data="price")],
    ]
    if MANAGER_URL.startswith("https://wa.me/"):
        buttons.append(
            [InlineKeyboardButton(text="👨🏻‍💻 Связаться с менеджером", url=MANAGER_URL)]
        )
    else:
        buttons.append(
            [InlineKeyboardButton(text="👨🏻‍💻 Связаться с менеджером", callback_data="contact")]
        )
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@dp.message(CommandStart())
async def start(message: Message) -> None:
    text = """🌟 Добро пожаловать в Академию Дошколят!

👶 Развивающая онлайн-программа для детей 4–6 лет.

Наша программа помогает развивать:
📚 Речь и навыки чтения
🧠 Логическое мышление
🎯 Внимание и память
❤️ Усидчивость и интерес к обучению
✍️ Навыки, необходимые для успешного старта в школе

🏠 Занимайтесь дома в удобное время.
⏰ Для занятий достаточно 15–20 минут в день.

🎥 В программе:
✅ 135 обучающих видеоуроков
✅ Развивающие игры и задания
✅ Уроки по безопасности и личной гигиене
✅ Рекомендации для родителей

👇 Выберите интересующий раздел:"""
    await message.answer(text, reply_markup=course_keyboard())


@dp.callback_query(F.data == "video")
async def send_video(callback: CallbackQuery) -> None:
    if VIDEO_PATH.is_file():
        await callback.message.answer_video(
            video=FSInputFile(VIDEO_PATH),
            caption="🎥 Пример урока Академии Дошколят",
        )
    else:
        await callback.message.answer("Демонстрационное видео временно недоступно.")
    await callback.answer()


@dp.callback_query(F.data == "price")
async def show_price(callback: CallbackQuery) -> None:
    text = """💰 Стоимость подписки на курс «Академия Дошколят»:

📚 Доступ на 3 месяца — 15 000 ₸
📚 Доступ на 6 месяцев — 20 000 ₸
📚 Доступ на 12 месяцев — 30 000 ₸"""
    if PAYMENT_INSTRUCTIONS:
        text += "\n\n" + PAYMENT_INSTRUCTIONS
    else:
        text += "\n\nДля оформления подписки свяжитесь с менеджером."

    keyboard = None
    if MANAGER_URL.startswith("https://wa.me/"):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="💬 Написать менеджеру", url=MANAGER_URL)]]
        )
    await callback.message.answer(text, reply_markup=keyboard)
    await callback.answer()


@dp.callback_query(F.data == "contact")
async def contact(callback: CallbackQuery) -> None:
    await callback.message.answer("Контакт менеджера пока не настроен.")
    await callback.answer()


async def main() -> None:
    if not TOKEN or TOKEN == "PASTE_YOUR_NEW_TOKEN_HERE":
        raise RuntimeError("Set TELEGRAM_BOT_TOKEN in your private .env file first.")
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
