from config.AppConst import AppConst
from helpers.PathHelper import PathHelper
from PIL import Image
import numpy
import os


class ImageGenerator:
    __IMAGE_HEIGHT = 100
    __IMAGE_WiDTH = 200

    def generate(self, filename):
        image = self.__create_image()
        image.save(os.path.join(PathHelper.get_image_folder(), filename))

        return self.__get_source_path(filename)

    def __get_image_path(self, filename):
        return PathHelper.get_image_folder() + filename

    def __create_image(self):
        rgb_array = numpy.random.rand(self.__IMAGE_HEIGHT, self.__IMAGE_WiDTH, 3) * 255
        image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')

        return image

    def __get_source_path(self, filename):
        return os.path.join(AppConst.IMAGE_SUBFOLDER, filename)
