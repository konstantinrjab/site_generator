from generators.SiteGenerator import SiteGenerator
from helpers.CleanupHelper import CleanupHelper

pages_count = 10
CleanupHelper().cleanup_site_folder()
SiteGenerator().generate(pages_count)
