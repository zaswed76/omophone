import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from telegram import ParseMode

from config_bot import API_TOKEN
import keyboards
import _diff
import settings

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


word_dict = _diff.get_words("corpora_noun.txt")








@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("введите слово для поиска")


@dp.message_handler()
async def echo_message(msg: types.Message):
    _text = msg.text.lower()
    if _text[0] == "/":
        res_comm = settings.do_setting(_text)
        await bot.send_message(msg.from_user.id, res_comm, parse_mode=ParseMode.HTML)
    else:
        res_pigment, flag = _diff.get_omo(_text, word_dict, settings.Settings.words, settings.Settings.ratio)

        await bot.send_message(msg.from_user.id, res_pigment, parse_mode=ParseMode.HTML)

#
#


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
