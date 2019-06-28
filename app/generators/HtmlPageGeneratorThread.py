from generators.HtmlPageGenerator import HtmlPageGenerator
from threading import Thread
from helpers.PathHelper import PathHelper
import os


class HtmlPageGeneratorThread(Thread):
    def __init__(self, name, references):
        self.__references = references
        self.__name = name
        super().__init__()

    def run(self):
        html_page = HtmlPageGenerator().generate(self.__references)
        self.__save_file(html_page)

    def __save_file(self, html_page):
        html_file = open(self.__get_file_path(), "w+")
        html_file.write(html_page)
        html_file.close()

    def __get_file_path(self):
        return os.path.join(PathHelper.get_site_folder(), self.__name)
