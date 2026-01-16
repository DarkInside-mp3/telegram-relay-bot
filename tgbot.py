import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "Привет! 👋\n"
        "Напиши сообщение, и я передам его администратору."
    )

@dp.message_handler()
async def forward_to_admin(message: types.Message):
    user = message.from_user
    username = f"@{user.username}" if user.username else "без username"

    text = (
        "📩 НОВОЕ СООБЩЕНИЕ\n\n"
        f"👤 Пользователь: {username}\n"
        f"🆔 ID: {user.id}\n\n"
        f"💬 Сообщение:\n{message.text}"
    )

    await bot.send_message(ADMIN_ID, text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
