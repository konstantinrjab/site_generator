from decorators.AbstractPairedTagDecorator import AbstractPairedTagDecorator


class SectionTag(AbstractPairedTagDecorator):
    NAME = 'section'

    def __init__(self, content):
        super().__init__(self.NAME, content)
