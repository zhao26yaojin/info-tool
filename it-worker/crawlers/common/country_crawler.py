from crawlers.cus_base import CusCrawlerBase
from models.common.country import Country

class CountryCrawler(CusCrawlerBase[Country]):
	def __init__(self):
		super().__init__('country')

	def crawl(self):
		pass


