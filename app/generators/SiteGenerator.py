from generators.HtmlPageGenerator import HtmlPageGenerator
from generators.StringGenerator import StringGenerator
import os


class SiteGenerator:
    SITE_FOLDER = '/site/'

    def generate(self, pages_count):
        file_names = self.__get_file_names(pages_count)
        for file_name in file_names:
            html_page = HtmlPageGenerator().generate(file_names)
            self.__save_file(html_page, file_name)

    def __get_file_names(self, pages_count):
        pages_names = []
        for page_number in range(pages_count):
            pages_names.append(StringGenerator().get_random_string() + ".html")
        return pages_names

    def __save_file(self, html_page, filename):
        html_file = open(self.__get_file_path(filename), "w+")
        html_file.write(html_page)
        html_file.close()

    def __get_file_path(self, filename):
        return os.getcwd() + self.SITE_FOLDER + filename
