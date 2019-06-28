from decorators.PairedTagDecorator import PairedTagDecorator


class TitleTag(PairedTagDecorator):
    NAME = 'title'

    def __init__(self, content):
        super().__init__(self.NAME, content)
