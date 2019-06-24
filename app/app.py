from generators.SiteGenerator import SiteGenerator
from helpers.CleanupHelper import CleanupHelper

pages_count = 10
CleanupHelper().site_folder()
SiteGenerator().generate(pages_count)
