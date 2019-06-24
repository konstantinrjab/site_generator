from decorators.AbstractPairedTagDecorator import AbstractPairedTagDecorator


class AnchorTag(AbstractPairedTagDecorator):
    NAME = 'a'

    def __init__(self, link):
        super().__init__(self.NAME, link, {'href': link})
