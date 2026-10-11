from crawlers.cus_base import CusCrawlerBase
from db.fb.tournament_db import TournamentDb
from models.fb.team import Team

class TeamCrawler(CusCrawlerBase[Team]):
	def __init__(self):
		super().__init__('team')

	def handle_request(self):
		pass


	def handle_rel_id(self):
		pending_items = [r for r in self.results if r.tournament_id is None]
		names = {r.tournament_name for r in pending_items}
		id_name_dict = TournamentDb().select_id_by_name(names) if names else {}

		for r in pending_items:
			r.tournament_id = id_name_dict.get(r.tournament_name)
		# 已有 id 的保留；新关联失败的丢弃
		self.results = [r for r in self.results if r.tournament_id is not None]

