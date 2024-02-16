from config import TOKEN
from rev import rev

import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import time


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello')

@dp.message(F.text)
async def rev_msg(message: Message):
    await message.answer(rev(message.text))



async def main():
    await dp.start_polling(bot)





if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

