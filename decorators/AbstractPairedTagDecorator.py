from abc import ABC


class AbstractPairedTagDecorator(ABC):
    def __init__(self, name, content):
        self._content = content
        self._name = name

    def get_formatted(self):
        return self.__generate_open_tag() + self._content + self.__generate_close_tag()

    def __generate_open_tag(self):
        return '<' + self._name + '>'

    def __generate_close_tag(self):
        return '</' + self._name + '>'
