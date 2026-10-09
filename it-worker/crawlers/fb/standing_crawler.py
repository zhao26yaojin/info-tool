from crawlers.cus_base import CusCrawlerBase
from db.fb.tournament_db import TournamentDb
from models.fb.standing import Standing

class StandingCrawler(CusCrawlerBase[Standing]):
	def __init__(self):
		super().__init__('standing')

	def crawl(self):
		self.handle_storage()

		self.handle_rel_id()

	def handle_storage(self):
		pass


	def handle_rel_id(self):
		tournament_names = [r.tournament_name for r in self.results]
		id_name_dict = TournamentDb().select_id_by_name(tournament_names)
		
		# 按名称关联 id; 找不到对应 id 的记录丢弃
		self.results = [r for r in self.results if r.tournament_name in id_name_dict]
		for r in self.results:
			r.id = id_name_dict[r.name]

