from tags.ParagraphTag import ParagraphTag
from tags.BodyTag import BodyTag
from tags.SectionTag import SectionTag
from tags.ImageTag import ImageTag
from tags.AnchorTag import AnchorTag
from generators.ImageGenerator import ImageGenerator
from generators.StringGenerator import StringGenerator
import lorem
import random


class BodyGenerator:
    __SECTIONS_COUNT = 5
    __IMG_FILENAME_LENGTH = 15

    def generate(self, references):
        sections = ''
        for sectionsCount in range(self.__SECTIONS_COUNT):
            sections += self.__generate_section(references)

        return BodyTag(sections).get_formatted()

    def __generate_section(self, references):
        paragraph = ParagraphTag(lorem.sentence()).get_formatted()
        a = AnchorTag(random.choice(references)).get_formatted()
        image = self.__get_image_tag()

        return SectionTag(paragraph + a + image).get_formatted()

    def __get_image_tag(self):
        filename = StringGenerator().get_random_string(self.__IMG_FILENAME_LENGTH) + '.jpg'

        return ImageTag(ImageGenerator().generate(filename), lorem.sentence()).get_formatted()
