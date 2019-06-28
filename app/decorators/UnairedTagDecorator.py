from decorators.AbstractTagDecorator import AbstractTagDecorator


class UnpairedTagDecorator(AbstractTagDecorator):
    _name = ''

    def __init__(self, name, attributes=None):
        self._name = name
        super().__init__(attributes)

    def get_formatted(self):
        return self.__get_open_tag() + self._get_attributes() + self.__get_close_tag()

    def __get_open_tag(self):
        return '<' + self._name

    def __get_close_tag(self):
        return '>'
