from config.AppConst import AppConst
import os


class PathHelper:
    @staticmethod
    def get_site_folder():
        return os.path.join(os.getcwd(), AppConst.SITE_DIRECTORY)

    @staticmethod
    def get_image_folder():
        return os.path.join(PathHelper.get_site_folder(), AppConst.IMAGE_SUBFOLDER)
