from generators.BodyGenerator import BodyGenerator
from generators.HeaderGenerator import HeaderGenerator


class HtmlPageGenerator:
    def generate_page(self):
        return self.__generate_header() + self.__generate_body()

    def __generate_header(self):
        return HeaderGenerator().generate()

    def __generate_body(self):
        return BodyGenerator().generate()
