from generators.HtmlPageGenerator import HtmlPageGenerator
from generators.StringGenerator import StringGenerator
import os


generator = HtmlPageGenerator()
html_page = generator.generate_page()
html_file = open(os.getcwd() + '/site/' + StringGenerator().get(10) + ".html", "w+")
html_file.write(html_page)
html_file.close()

print(html_page)
