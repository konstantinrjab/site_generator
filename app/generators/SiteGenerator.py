from generators.HtmlPageGenerator import HtmlPageGenerator
from generators.StringGenerator import StringGenerator
import os


class SiteGenerator:
    SITE_FOLDER = '/site/'

    def generate(self, pages_count):
        for page_number in range(pages_count):
            filename = StringGenerator().get_random_string()
            html_page = HtmlPageGenerator().generate()
            self.__save_file(html_page, filename)

        return True

    def __save_file(self, html_page, filename):
        html_file = open(self.__get_file_path(filename), "w+")
        html_file.write(html_page)
        html_file.close()

    def __get_file_path(self, filename):
        return os.getcwd() + self.SITE_FOLDER + filename + ".html"
