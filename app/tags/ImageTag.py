from decorators.UnairedTagDecorator import UnpairedTagDecorator


class ImageTag(UnpairedTagDecorator):
    __NAME = 'img'

    def __init__(self, source, alt=''):
        self.__src = source
        self.__alt = alt
        super().__init__(self.__NAME, {'src': source, 'alt': alt})
