from aiogram import Bot, Dispatcher, Types
from aiogram.utils import executor

API_TOKEN = "TOKEN"


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply("Здарова педеки")