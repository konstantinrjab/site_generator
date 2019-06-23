from decorators.AbstractPairedTagDecorator import AbstractPairedTagDecorator


class HeadTag(AbstractPairedTagDecorator):
    __NAME = 'head'

    def __init__(self, content):
        super().__init__(self.__NAME, content)
