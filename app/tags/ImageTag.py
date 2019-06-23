class ImageTag:
    __NAME = 'img'
    __src = ''
    __alt = ''

    def __init__(self, source, alt=''):
        self.__src = source
        self.__alt = alt

    def get_formatted(self):
        return '<' + self.__NAME + self.__get_source_attribute() + self.__get_alt_attribute() + '/>'

    def __get_source_attribute(self):
        return ' src="' + self.__src + '" '

    def __get_alt_attribute(self):
        return ' alt="' + self.__alt + '" '
