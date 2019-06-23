from generators.BodyGenerator import BodyGenerator
from generators.HeaderGenerator import HeaderGenerator


class HtmlPageGenerator:
    def generate(self):
        return '<!doctype html><html lang="en">' + self.__head() + self.__body()+'</html>'

    def __head(self):
        return HeaderGenerator().generate()

    def __body(self):
        return BodyGenerator().generate()
