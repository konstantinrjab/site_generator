class ImageTag:
    NAME = 'img'
    __link = ''

    def __init__(self, source):
        self.__link = source

    def get_formatted(self):
        return '<' + self.NAME + self.__get_source_attribute() + '/>'

    def __get_source_attribute(self):
        return ' src="' + self.__link + '" '
