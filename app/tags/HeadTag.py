from decorators.PairedTagDecorator import PairedTagDecorator


class HeadTag(PairedTagDecorator):
    __NAME = 'head'

    def __init__(self, content):
        super().__init__(self.__NAME, content)
