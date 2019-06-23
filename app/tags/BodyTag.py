from decorators.AbstractPairedTagDecorator import AbstractPairedTagDecorator


class BodyTag(AbstractPairedTagDecorator):
    NAME = 'body'

    def __init__(self, content):
        super().__init__(self.NAME, content)
