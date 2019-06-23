from generators.HtmlPageGenerator import HtmlPageGenerator
from generators.StringGenerator import StringGenerator
import os


class SiteGenerator:
    SITE_FOLDER = '/site/'

    def generate(self):
        html_page = HtmlPageGenerator().generate()
        self.__save_file(html_page)
        return html_page

    def __save_file(self, html_page):
        html_file = open(self.__get_file_name(), "w+")
        html_file.write(html_page)
        html_file.close()

    def __get_file_name(self):
        return os.getcwd() + self.SITE_FOLDER + StringGenerator().get_random_string(10) + ".html"
