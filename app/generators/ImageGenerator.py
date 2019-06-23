from tags.ImageTag import ImageTag
from generators.StringGenerator import StringGenerator
from PIL import Image
import lorem
import numpy
import os


class ImageGenerator:
    FILENAME_LENGTH = 10
    IMAGE_DIRECTORY = '/site/img/'
    IMAGE_SOURCE_PATH = '/img/'
    IMAGE_HEIGHT = 100
    IMAGE_WiDTH = 200

    def generate(self):
        image = self.__create_image()
        filename = self.__get_filename()
        image.save(self.__get_image_path(filename))

        return ImageTag(self.__get_image_source_tag(filename), lorem.sentence()).get_formatted()

    def __get_image_path(self, filename):
        return os.getcwd() + self.IMAGE_DIRECTORY + filename

    def __create_image(self):
        rgb_array = numpy.random.rand(self.IMAGE_HEIGHT, self.IMAGE_WiDTH, 3) * 255
        image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')

        return image

    def __get_image_source_tag(self, filename):
        return self.IMAGE_SOURCE_PATH + filename

    def __get_filename(self):
        return StringGenerator().get_random_string(self.FILENAME_LENGTH) + '.jpg'
