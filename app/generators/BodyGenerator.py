from tags.ParagraphTag import ParagraphTag
from tags.BodyTag import BodyTag
from generators.ImageGenerator import ImageGenerator
import lorem


class BodyGenerator:
    SECTIONS_COUNT = 2

    def generate(self):
        sections = ''
        for sectionsCount in range(self.SECTIONS_COUNT):
            sections += self.__generate_section()

        return BodyTag(sections).get_formatted()

    def __generate_section(self):
        paragraph = ParagraphTag(lorem.sentence()).get_formatted()
        image = ImageGenerator().generate()

        return paragraph + image
