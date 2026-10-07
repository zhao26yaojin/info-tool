from db.db_base import DbBase
from models.fb.team import Team

class TeamDb(DbBase[Team]):
	upsert_sql: str = """
        INSERT INTO fb_team (id, name, country_name, source_id)
        VALUES (%s, %s, %s, %s) AS new
        ON DUPLICATE KEY UPDATE
            name = new.name,
			country_name = new.country_name;
    """

	insert_sql: str = """
            INSERT INTO fb_team (id, name, country_name, source_id)
            VALUES (%s, %s, %s, %s)
        """

	select_source_ids_sql: str = """
            SELECT source_id
            FROM fb_team
        """

	delete_sql: str = """
            DELETE FROM fb_team
            WHERE id = %s
        """

	def to_upsert_params(self, item: Team):
		return item.id, item.name, item.country_name, item.source_id

	def to_insert_params(self, item: Team):
		return item.id, item.name, item.country_name, item.source_id

