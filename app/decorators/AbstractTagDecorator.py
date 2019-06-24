from abc import ABC


class AbstractTagDecorator(ABC):
    _attributes = []

    def __init__(self, attributes=None):
        self._attributes = attributes if attributes is not None else []

    def _get_attributes(self):
        if not self._attributes:
            return ''
        attributes = ''
        for name, value in self._attributes.items():
            attributes += ' ' + name + '="' + value + '" '

        return attributes
