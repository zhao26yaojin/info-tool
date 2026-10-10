from db.db_base import DbBase
from models.fb.team import Team

class TeamDb(DbBase[Team]):
	upsert_sql: str = """
        INSERT INTO fb_team (id, name, source_id, logo)
        VALUES (%s, %s, %s, %s) AS new
        ON DUPLICATE KEY UPDATE
            name = new.name,
			logo = new.logo;
    """

	insert_sql: str = """
            INSERT INTO fb_team (id, name, source_id, logo)
            VALUES (%s, %s, %s, %s)
        """

	select_source_ids_sql: str = """
            SELECT source_id
            FROM fb_team
        """

	delete_sql: str = """
            DELETE FROM fb_team
            WHERE source_id IN %s
        """

	select_source_id_by_name_sql: str = """
            SELECT source_id, name
            FROM fb_team
            WHERE name IN %s
        """

	def to_upsert_params(self, item: Team):
		return item.id, item.name, item.source_id, item.logo

	def to_insert_params(self, item: Team):
		return item.id, item.name, item.source_id, item.logo

