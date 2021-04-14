import Levenshtein as lv


class Word:
    def __init__(self, word, ratio):
        self.ratio = ratio
        self.word = word


class NCSort:
    ByFirstSymbols = "FirstSymbols"
    ByRatio = "Ratio"

    @staticmethod
    def ByRatio(seq, reverse=True):
        res = sorted(seq, key=lambda w: w[1], reverse=reverse)
        return [x[0] for x in res]

    @staticmethod
    def ByFirstSymbols(seq, symb, reverse=False):
        rat = NCSort.ByRatio(seq)
        for smb in symb:
            rat.sort(key=lambda x: not smb in x, reverse=reverse)
        return rat


class NCSearch:
    ON_RATIO = "on_ratio"

    def __init__(self, word_list=None):
        """

        :type dictionary: list список слов
        """
        if word_list is not None:
            self.word_list = word_list
        else:
            self.word_list = list()

    def jaro_winkler(self, **kwargs):
        """

        :param kwargs:
        :return: список кортежей [(str, float), (слово, рейтинг)]
        """
        word_list = kwargs.get("word_list", self.word_list)
        word = kwargs["word"]
        ratio = kwargs.get("ratio", 0.6)
        prefix_weight = kwargs.get("prefix_weight", 0.3)
        sort = kwargs.get("sort", None)

        self.result = []
        for line in word_list:
            r = lv._levenshtein.jaro_winkler(word, line, prefix_weight)
            if r > ratio:
                self.result.append((line, r))

        if sort is not None:
            sort_res = getattr(NCSort, sort[0])(self.result, sort[1])

        else:
            sort_res = self.result
        return sort_res


if __name__ == '__main__':
    nc = NCSearch()

    d = dict(word="курола", word_list=["прод", "корава", "коравай", "каравай", "кровь", "каровища", "урва", "коркалол"])

    r = nc.jaro_winkler(**d)
    # sort = NCSort.sorte(r, NCSort.ByRatio)
    sort2 = NCSort.ByFirstSymbols(r, ("ка", "кар","ко", "кор", "кора"))
    print(sort2)
