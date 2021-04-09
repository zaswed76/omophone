class Settings:
    words = 100
    ratio = 60


def set_count_words(count):
    if not count.isdigit():
        return "не верное значение {}".format(count)
    count = int(count)
    if count <= 0:
        return "должно быть больше 0".format(count)
    else:
        Settings.words = count
        return "установлено колличество слов - {}".format(count)


def set_ratio(ratio):
    if not ratio.isdigit():
        return "не верное значение {}".format(ratio)
    count = int(ratio)
    if count <= 0:
        return "должно быть больше 0".format(count)
    else:
        Settings.ratio = ratio
        return "установлен рейтинг поиска - {}".format(ratio)


commands = {"/words": set_count_words, "/ratio": set_ratio}


def do_setting(command: str):
    for name, comm in commands.items():
        if command.startswith(name):
            v = command.split(name)[-1].strip()
            return comm(v)
    else:
        com_lst = "\n".join(list(commands.keys()))
        return "команда не найдена\nдостуные команды:\n{}".format(com_lst)
