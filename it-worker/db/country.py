from typing import Tuple

from db.base import DbBase
from models.country import Country


class CountryDb(DbBase[Country]):
    upsert_sql: str = """
            INSERT INTO common_country (id, name)
            VALUES (%s, %s, %s, NOW())
            ON DUPLICATE KEY UPDATE
                name = VALUES(name),
                league = VALUES(league),
                updated_at = NOW();
        """

    select_source_ids_sql: str = """
            SELECT source_id
            FROM teams
            WHERE country = %s
        """

    soft_delete_sql: str = """
            UPDATE sports_teams 
            SET status = 0 
            WHERE team_id IN %s
        """

    delete_sql: str = """
            DELETE FROM teams
            WHERE id = %s
        """

    insert_sql: str = """
            INSERT INTO teams (name, country)
            VALUES (%s, %s)
        """

    # 2. 定义数据提取映射逻辑
    def to_upsert_params(self, item: Country) -> Tuple:
        return (item.id, item.name)

    def to_insert_params(self, item: Country) -> Tuple:
        return (item.id, item.name)

    def get_entity_id(self, item: Country) -> int:
        return item.id
