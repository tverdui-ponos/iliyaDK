from aiogram import F
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.enums import ParseMode

from aiogram.client.default import DefaultBotProperties

import asyncio



def token_read():
    with open("token.txt", "r") as file: return file.readline()

API_TOKEN = token_read()



dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer("Здарова педеки")

@dp.message(F.text, Command("where_is_Iliya"))
async def where(message:Message) -> None:
    await message.reply("В <strong> пизде </strong>")




async def main() -> None:
    bot = Bot(token=API_TOKEN, 
    default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())