from decorators.AbstractPairedTagDecorator import AbstractPairedTagDecorator


class ParagraphTag(AbstractPairedTagDecorator):
    NAME = 'p'

    def __init__(self, content):
        super().__init__(self.NAME, content)
