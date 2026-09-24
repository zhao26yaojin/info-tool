from db.db_base import DbBase
from models.fb.team import Team

class TeamDb(DbBase[Team]):
	upsert_sql: str = """
        INSERT INTO fb_team (id, name, league, created_at)
        VALUES (%s, %s, %s, NOW())
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            league = VALUES(league),
            updated_at = NOW();
    """

	def to_upsert_params(self, item: Team):
		return (item.id, item.league_id, item.name)
