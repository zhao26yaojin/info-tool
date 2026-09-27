from db.db_base import DbBase
from models.common.country import Country

class CountryDb(DbBase[Country]):
	upsert_sql: str = """
        INSERT INTO common_country (id, name, avatar, source_id)
        VALUES (%s, %s, %s, %s) AS row
        ON DUPLICATE KEY UPDATE
            name = row.name,
			avatar = row.avatar;
    """

	insert_sql: str = """
            INSERT INTO common_country (id, name, avatar, source_id)
            VALUES (%s, %s, %s, %s)
        """

	select_source_ids_sql: str = """
            SELECT source_id
            FROM common_country
        """

	delete_sql: str = """
            DELETE FROM common_country
            WHERE id = %s
        """

	def to_upsert_params(self, item: Country):
		return item.id, item.name, item.avatar, item.source_id

	def to_insert_params(self, item: Country):
		return item.id, item.name, item.avatar, item.source_id

