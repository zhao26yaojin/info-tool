from crawlers.cus_base import CusCrawlerBase
from models.fb.tournament import Tournament

class TournamentCrawler(CusCrawlerBase[Tournament]):
	def __init__(self):
		super().__init__('tournament')

	def handle_request(self):
		pass


