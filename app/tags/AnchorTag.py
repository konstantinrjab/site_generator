from decorators.PairedTagDecorator import PairedTagDecorator


class AnchorTag(PairedTagDecorator):
    NAME = 'a'

    def __init__(self, link):
        super().__init__(self.NAME, link, {'href': link})
