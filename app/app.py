from generators.SiteGenerator import SiteGenerator
from helpers.CleanupHelper import CleanupHelper

CleanupHelper().site_folder()
print(SiteGenerator().generate(5))
