import logging
from enum import Enum

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from telegram import ParseMode

from config_bot import API_TOKEN
import keyboards

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

class Status:
    find = "find"
    words = "words"
    ratio = "ratio"
    current = find

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("введите слово для поиска")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("программа умеет искать слова похожие по звучанию", reply_markup=keyboards.help_btns())

@dp.message_handler(commands=['words'])
async def start(message: types.Message):
    await message.answer("укажите колличество - число от 1 до 200")

@dp.message_handler(commands=['ratio'])
async def start(message: types.Message):
    await message.answer("укажите рейтинг - число от 0 до 100")

@dp.message_handler()
async def echo_message(msg: types.Message):

    await bot.send_message(msg.from_user.id, "res_pigment_str", parse_mode=ParseMode.HTML)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)