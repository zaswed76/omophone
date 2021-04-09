

from aiogram import Bot, Dispatcher, executor, types
def range_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("ввести диапазон")
    return keyboard

def menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("начать", "перемешать и начать")
    keyboard.add("ввести диапазон")
    return keyboard