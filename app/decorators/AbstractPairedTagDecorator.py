from abc import ABC


class AbstractPairedTagDecorator(ABC):
    _content = ''

    def __init__(self, name, content):
        self._content = content
        self._name = name

    def get_formatted(self):
        return self.__get_open_tag() + self._content + self.__get_close_tag()

    def __get_open_tag(self):
        return '<' + self._name + '>'

    def __get_close_tag(self):
        return '</' + self._name + '>'
