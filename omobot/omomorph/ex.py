from enum import Enum


class Status:
    find = "find"
    words = "words"
    ratio = "ratio"
    current = find



    # @property
    # def current(self):
    #     return self._current
    #
    # @current.setter
    # def current(self, v):
    #     self._current = v


print(Status.current)
Status.current = Status.words
print(Status.current)
