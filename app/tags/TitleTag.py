from decorators.AbstractPairedTagDecorator import AbstractPairedTagDecorator


class TitleTag(AbstractPairedTagDecorator):
    NAME = 'title'

    def __init__(self, content):
        super().__init__(self.NAME, content)
