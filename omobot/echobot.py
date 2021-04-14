import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from telegram import ParseMode

from config_bot import API_TOKEN
import keyboards
import _diff
import settings
from omomorph import ncsearch

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def get_words(file):
    with open(file, "r", encoding="utf-8") as f:
        return [x.strip() for x in f.readlines()]

def split2(word: str, sep):
    return word.replace(sep, "<b>{}</b>".format(sep.upper()))

word_dict = get_words("corpora_noun.txt")

nc = ncsearch.NCSearch(word_dict)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("введите слово для поиска")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("программа умеет искать слова похожие по звучанию", reply_markup=keyboards.help_btns())

@dp.message_handler()
async def echo_message(msg: types.Message):
    print(msg.from_user.id)
    _text = msg.text.lower()
    if _text[0] == "/":
        res_comm = settings.do_setting(_text)
        await bot.send_message(msg.from_user.id, res_comm, parse_mode=ParseMode.HTML)
    else:
        option = dict(word=_text, word_list=word_dict)
        res = nc.jaro_winkler(**option)
        if res:
            sort = ncsearch.NCSort.ByFirstSymbols(res, (_text[:2], _text[:3], _text[:4]))
            sort_cut = sort[:int(settings.Settings.words)]
            max_len = sorted(sort_cut, key=len)[-1]
            res_pigment = [split2(x, _text[:3]) for x in sort_cut]
        #
        # print(res_pigment)
        # print("----------------------")
        # print(max_len)

            res_pigment_str = "      ".join(res_pigment)
        # res_pigment_str = "      ".join(["pigment"]*59)

            await bot.send_message(msg.from_user.id, res_pigment_str, parse_mode=ParseMode.HTML)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
