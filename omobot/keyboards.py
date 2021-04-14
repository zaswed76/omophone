

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def range_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("ввести диапазон")
    return keyboard

def menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("начать", "перемешать и начать")
    keyboard.add("ввести диапазон")
    return keyboard


def help_btns():
    inline_kb1 = InlineKeyboardMarkup()
    inline_btn_1 = InlineKeyboardButton('1', callback_data='button1')
    inline_btn_2 = InlineKeyboardButton('2', callback_data='button1')
    inline_btn_3 = InlineKeyboardButton('3', callback_data='button1')
    inline_kb1.add(inline_btn_1)
    inline_kb1.add(inline_btn_2)
    inline_kb1.add(inline_btn_3)
    return inline_kb1
