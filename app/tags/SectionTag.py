from decorators.PairedTagDecorator import PairedTagDecorator


class SectionTag(PairedTagDecorator):
    NAME = 'section'

    def __init__(self, content):
        super().__init__(self.NAME, content)
