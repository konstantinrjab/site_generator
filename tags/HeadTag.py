from decorators.AbstractPairedTagDecorator import AbstractPairedTagDecorator


class HeadTag(AbstractPairedTagDecorator):
    NAME = 'head'

    def __init__(self, content):
        super().__init__(self.NAME, content)
