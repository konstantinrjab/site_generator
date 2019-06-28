from decorators.UnairedTagDecorator import UnpairedTagDecorator


class MetaTag(UnpairedTagDecorator):
    NAME = 'meta'

    def __init__(self, attributes):
        super().__init__(self.NAME, attributes)
