import os


class CleanupHelper:
    __SITE_FOLDER = os.getcwd() + '/site'
    __IMAGE_SUBFOLDER = '/img/'

    def site_folder(self):
        for file in self.__get_files():
            try:
                if os.path.isfile(file):
                    os.unlink(file)
            except Exception as e:
                print(e)

    def __get_files(self):
        site_folder = self.__SITE_FOLDER
        site_folder = site_folder + self.__IMAGE_SUBFOLDER
        files = []
        files.extend(self.__get_html_files(site_folder))
        files.extend(self.__get_image_files(site_folder))

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
