from generators.BodyGenerator import BodyGenerator
from generators.HeaderGenerator import HeaderGenerator


class HtmlPageGenerator:
    def generate(self, references):
        return '<!doctype html><html lang="en">' + self.__head() + self.__body(references)+'</html>'

    def __head(self):
        return HeaderGenerator().generate()

    def __body(self, references):
        return BodyGenerator().generate(references)
