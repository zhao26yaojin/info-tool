from db.db_base import DbBase
from models.common.country import Country

class CountryDb(DbBase[Country]):
	upsert_sql: str = """
        INSERT INTO common_country (id, name, league, created_at)
        VALUES (%s, %s, %s, NOW())
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            league = VALUES(league),
            updated_at = NOW();
    """

	def to_upsert_params(self, item: Country):
		return (item.id, item.league_id, item.name)
