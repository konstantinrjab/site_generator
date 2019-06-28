from generators.HtmlPageGeneratorThread import HtmlPageGeneratorThread
from generators.StringGenerator import StringGenerator


class SiteGenerator:
    def generate(self, pages_count):
        page_names = self.__get_page_names(pages_count)
        for page_name in page_names:
            thread = HtmlPageGeneratorThread(page_name, page_names)
            thread.run()

    def __get_page_names(self, pages_count):
        pages_names = []
        for page_number in range(pages_count):
            pages_names.append(StringGenerator().get_random_string() + ".html")

        return pages_names
