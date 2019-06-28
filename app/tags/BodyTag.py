from decorators.PairedTagDecorator import PairedTagDecorator


class BodyTag(PairedTagDecorator):
    NAME = 'body'

    def __init__(self, content):
        super().__init__(self.NAME, content)
