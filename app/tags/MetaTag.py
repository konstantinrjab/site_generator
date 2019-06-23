from decorators.AbstractUnairedTagDecorator import AbstractUnpairedTagDecorator


class MetaTag(AbstractUnpairedTagDecorator):
    NAME = 'meta'

    def __init__(self, attributes):
        super().__init__(self.NAME, attributes)
