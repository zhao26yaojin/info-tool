from db.db_base import DbBase
from models.common.country import Country

class CountryDb(DbBase[Country]):
	upsert_sql: str = """
        INSERT INTO common_country (id, name, logo, source_id)
        VALUES (%s, %s, %s, %s) AS new
        ON DUPLICATE KEY UPDATE
            name = new.name,
			logo = new.logo;
    """

	insert_sql: str = """
            INSERT INTO common_country (id, name, logo, source_id)
            VALUES (%s, %s, %s, %s)
        """

	select_source_ids_sql: str = """
            SELECT source_id
            FROM common_country
        """

	delete_sql: str = """
            DELETE FROM common_country
            WHERE source_id IN %s
        """

	select_source_id_by_name_sql: str = """
            SELECT source_id, name
            FROM common_country
            WHERE name IN %s
        """

	def to_upsert_params(self, item: Country):
		return item.id, item.name, item.logo, item.source_id

	def to_insert_params(self, item: Country):
		return item.id, item.name, item.logo, item.source_id

