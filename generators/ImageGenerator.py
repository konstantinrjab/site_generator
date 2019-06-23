from tags.ImageTag import ImageTag
from PIL import Image
from generators.StringGenerator import StringGenerator
import numpy
import os


class ImageGenerator:
    FILENAME_LENGTH = 10
    IMAGE_DIRECTORY = '/site/img/'
    IMAGE_SOURCE_PATH = '/img/'
    IMAGE_HEIGHT = 100
    IMAGE_WiDTH = 200

    def generate(self):
        rgb_array = numpy.random.rand(self.IMAGE_HEIGHT, self.IMAGE_WiDTH, 3) * 255
        image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')

        filename = self.__get_filename()
        image.save(os.getcwd() + self.IMAGE_DIRECTORY + filename)

        return ImageTag(self.IMAGE_SOURCE_PATH + filename).get_formatted()

    def __get_filename(self):
        return StringGenerator().get_random_string(self.FILENAME_LENGTH) + '.jpg'
