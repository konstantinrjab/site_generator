from decorators.AbstractTagDecorator import AbstractTagDecorator


class PairedTagDecorator(AbstractTagDecorator):
    _content = ''

    def __init__(self, name, content, attributes=None):
        self._content = content
        self._name = name
        super().__init__(attributes)

    def get_formatted(self):
        return self.__get_open_tag() + self._content + self.__get_close_tag()

    def __get_open_tag(self):
        return '<' + self._name + self._get_attributes() + '>'

    def __get_close_tag(self):
        return '</' + self._name + '>'
