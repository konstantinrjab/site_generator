from tags.ParagraphTag import ParagraphTag
from tags.BodyTag import BodyTag
from tags.SectionTag import SectionTag
from tags.AnchorTag import AnchorTag
from generators.ImageGenerator import ImageGenerator
import lorem
import random


class BodyGenerator:
    __SECTIONS_COUNT = 5

    def generate(self, references):
        sections = ''
        for sectionsCount in range(self.__SECTIONS_COUNT):
            sections += self.__generate_section(references)

        return BodyTag(sections).get_formatted()

    def __generate_section(self, references):
        paragraph = ParagraphTag(lorem.sentence()).get_formatted()
        a = AnchorTag(random.choice(references)).get_formatted()
        image = ImageGenerator().generate()
        section = SectionTag(paragraph + a + image).get_formatted()

        return section
