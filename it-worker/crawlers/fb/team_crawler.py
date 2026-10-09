from crawlers.cus_base import CusCrawlerBase
from models.fb.team import Team

class TeamCrawler(CusCrawlerBase[Team]):
	def __init__(self):
		super().__init__('team')

	def handle_request(self):
		pass


