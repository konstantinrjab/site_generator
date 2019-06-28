import os
from helpers.PathHelper import PathHelper


class CleanupHelper:
    __SITE_FOLDER = os.getcwd() + '/../site'
    __IMAGE_SUBFOLDER = '/img/'

    def site_folder(self):
        for file in self.__get_files():
            try:
                if os.path.isfile(file):
                    os.unlink(file)
            except Exception as e:
                print(e)

    def __get_files(self):
        files = []
        files.extend(self.__get_html_files(PathHelper.get_site_folder()))
        files.extend(self.__get_image_files(PathHelper.get_image_folder()))

        return files

    def __get_html_files(self, folder):
        html_files = []
        for file in os.listdir(folder):
            if file.endswith('.html'):
                html_files.append(os.path.join(folder, file))
        return html_files

    def __get_image_files(self, folder):
        image_files = []
        for file in os.listdir(folder):
            if file.endswith('.jpg'):
                image_files.append(os.path.join(folder, file))
        return image_files
