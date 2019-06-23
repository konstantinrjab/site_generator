from abc import ABC


class AbstractUnpairedTagDecorator(ABC):
    _name = ''
    _attributes = []

    def __init__(self, name, attributes):
        self._attributes = attributes
        self._name = name

    def get_formatted(self):
        return self.__get_open_tag() + self.__get_attributes() + self.__get_close_tag()

    def __get_open_tag(self):
        return '<' + self._name

    def __get_close_tag(self):
        return '>'

    def __get_attributes(self):
        attributes = ''
        for name, value in self._attributes.items():
            attributes += ' ' + name + '="' + value + '" '

        return attributes
