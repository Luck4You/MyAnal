from ddl.bot_text import __help
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5602787567:AAGYv7NrSjwyW7qPs_yvu70C060zrcfZDbQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ Эхо-бот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")
 
@dp.message_handler()
async def echo(message: types.Message):
   await message.answer(message.text)
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)