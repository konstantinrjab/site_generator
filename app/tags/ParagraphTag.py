from decorators.PairedTagDecorator import PairedTagDecorator


class ParagraphTag(PairedTagDecorator):
    NAME = 'p'

    def __init__(self, content):
        super().__init__(self.NAME, content)
