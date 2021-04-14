from itertools import zip_longest

import Levenshtein as lv
import numpy as np


def get_words(file):
    with open(file, "r", encoding="utf-8") as f:
        return [x.strip() for x in f.readlines()]


def grouper(n, iterable, fillvalue=""):
    args = [iter(iterable)] * n
    spl = list(zip_longest(fillvalue=fillvalue, *args))
    a = np.array(spl)
    return a.transpose()


def sorted_on_ratio(iterable, reverse=True):
    return sorted(iterable, key=lambda w: w[1], reverse=reverse)
    # print(r)
    # return [x[0] for x in r]


def file_to_words(file):
    """
    получить список слов из файла
    :param file: path
    :return: дшые
    """
    with open(file, "r", encoding="utf-8") as f:
        return [x.strip() for x in f]


def get_omo(_text, word_dict, count_words, ratio):
    """


    :type ratio: int 0-100
    :type count_words: int > 0
    :type word_dict: list < str словарь в виде списка слов
    :type _text: str слово для поиск
    """
    omo_list_with_ratio = __get_omo("jaro", word_dict, _text, ratio)
    res_sort = sorted_on_ratio(omo_list_with_ratio)
    omo_list_not_ratio = [x[0] for x in res_sort if x][:int(count_words)]
    res_pigment = [split2(x, _text[:3]) for x in omo_list_not_ratio]
    if not res_pigment:
        return """нет результатов
        попробуйте другое слово или понизьте рейтинг совпадения
        текущий - {}
        установить рейтинг - /ratio значение""".format(
            ratio), False
    else:
        return "    ".join(res_pigment), True


def test():
    res = []
    for i in range(200000):
        r = lv._levenshtein.jaro_winkler("трава", "дрова", 0.01)
        res.append(r)
    return res[0]


def Jaro(**kwargs):
    """

    :param kwargs:
    :return: список кортежей [(str, float), (слово, рейтинг)]
    """
    lst = kwargs["lst"]
    word = kwargs["word"]
    ratio = kwargs["ratio"]
    prefix_weight = kwargs["prefix_weight"]

    result = []
    ratio = float(ratio) / 100

    for line in lst:
        r = lv._levenshtein.jaro_winkler(word, line, prefix_weight)

        if r > ratio:
            result.append((line, r))
    return result


def Intellect(**kwargs):
    lst = kwargs["lst"]
    word = kwargs["word"]
    ratio = kwargs["ratio"]
    result = []
    ratio = float(ratio) / 100
    for line in lst:
        r = lv._levenshtein.jaro(word, line)
        if r > ratio:
            result.append((line, r))
    return result


def Ratio(**kwargs):
    lst = kwargs["lst"]
    word = kwargs["word"]
    ratio = kwargs["ratio"]
    result = []
    ratio = float(ratio) / 100
    for line in lst:
        r = lv._levenshtein.ratio(word, line)
        if r > ratio:
            result.append((line, r))
    return result


def find(lst, *words):
    d = {}
    for w in words:
        try:
            i = lst.index(w)
        except ValueError:
            print("{} not".format(w))
        else:
            d[w] = i
    return d


def find2(seq, word):
    for n, (w, r) in enumerate(seq):
        # print(item)
        if w == word:
            return "{}.{}, {}".format(n, w, r)
    else:
        return "не найдено"


def __get_omo(algorithm, word_dict, word, ratio=70):
    return diff_functions[algorithm](lst=word_dict, word=word, ratio=ratio, prefix_weight=0.2)


diff_functions = dict(
    Intellect=Intellect,
    jaro=Jaro,
    ratio=Ratio
)


def split(word: str, sep):
    r = [x for x in word.partition(sep) if x]
    print(r)
    l = len(r)
    if word == sep:
        return "<b>{}</b>".format(r[0].swapcase())
    if l == 2:
        return "<b>{}</b>{}".format(r[0].swapcase(), r[1])
    elif l == 3:
        return "{}<b>{}</b>{}".format(r[0], r[1].swapcase(), r[2])
    else:
        return word


def split2(word: str, sep):
    return word.replace(sep, "<b>{}</b>".format(sep.upper()))


if __name__ == '__main__':
    print(split2("eкор", "кор"))
    print("###################")
    # opcorpora_noun_file = pjoin(r"E:\1_SYNS_ORIGINAL\0SYNC\Serg\note_tab\notetub\dictionaries\corpora_noun.txt")
    # corp = file_to_words(opcorpora_noun_file)
    #
    # dct = dict(lst=corp, word="карофа",  ratio=40, prefix_weight=0.2)
    # r = jaro_winkler(**dct)
    # # r = jaro(corp, "ден!м!",  65)
    # print(find2(sorted_on_ratio(r)[:1500], "корова"))
