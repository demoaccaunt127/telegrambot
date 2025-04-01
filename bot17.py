import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

# Loglarni sozlash
logging.basicConfig(level=logging.INFO)

# Bot tokenini to‘g‘ridan-to‘g‘ri kodga yozamiz
TOKEN = "7525614605:AAH3IW2KV-oCmJGOHtxZQIVTOwgQ7OPMFpY"

# Bot va Dispatcher obyektlarini yaratamiz
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Tugma yaratamiz
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ECLIN DECOR ga kirish", url="https://eclindecorbot.netlify.app")]
])

# /start buyrug'iga javob beruvchi funksiya
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("ECLIN DECOR ga kirish uchun pastdagi tugmani bosing", reply_markup=keyboard)

# Botni ishga tushirish
async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # Eski xabarlarni o‘chirish
    await dp.start_polling(bot)  # Pollingni ishga tushirish

if __name__ == "__main__":
    asyncio.run(main())
