import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

API_BOT="8848273221:AAH5pZ5zwZZ95EPAfG3p_1LIwZWgkd1chIo"

bot = Bot(API_BOT)
dp = Dispatcher()
async def main():
    print("Bot Start")
    await dp.start_polling(bot)    


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет, я твой первый бот!")

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Я готов помогать!")

if __name__ == '__main__':
    asyncio.run(main())