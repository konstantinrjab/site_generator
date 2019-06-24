from tags.ParagraphTag import ParagraphTag
from tags.BodyTag import BodyTag
from tags.SectionTag import SectionTag
from generators.ImageGenerator import ImageGenerator
import lorem


class BodyGenerator:
    __SECTIONS_COUNT = 5

    def generate(self):
        sections = ''
        for sectionsCount in range(self.__SECTIONS_COUNT):
            sections += self.__generate_section()

        return BodyTag(sections).get_formatted()

    def __generate_section(self):
        paragraph = ParagraphTag(lorem.sentence()).get_formatted()
        image = ImageGenerator().generate()
        section = SectionTag(paragraph + image).get_formatted()

        return section
