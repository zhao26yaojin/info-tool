from db.db_base import DbBase
from models.fb.tournament import Tournament

class TournamentDb(DbBase[Tournament]):
	upsert_sql: str = """
        INSERT INTO fb_tournament (id, name, source_id, logo)
        VALUES (%s, %s, %s, %s) AS new
        ON DUPLICATE KEY UPDATE
            name = new.name,
			logo = new.logo;
    """

	insert_sql: str = """
            INSERT INTO fb_tournament (id, name, source_id, logo)
            VALUES (%s, %s, %s, %s)
        """

	select_source_ids_sql: str = """
            SELECT source_id
            FROM fb_tournament
        """

	delete_sql: str = """
            DELETE FROM fb_tournament
            WHERE source_id IN %s
        """

	select_id_by_name_sql: str = """
            SELECT id, name
            FROM fb_tournament
            WHERE name IN %s
        """

	def to_upsert_params(self, item: Tournament):
		return item.id, item.name, item.source_id, item.logo

	def to_insert_params(self, item: Tournament):
		return item.id, item.name, item.source_id, item.logo

