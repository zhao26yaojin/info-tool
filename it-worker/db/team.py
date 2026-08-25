from typing import Tuple

from models.team import Team
from .base import DbBase


class TeamDb(DbBase[Team]):
    upsert_sql = """
        INSERT INTO sports_teams (team_id, league_id, name, status) 
        VALUES (%s, %s, %s, 1)
        ON DUPLICATE KEY UPDATE name = VALUES(name), status = 1
    """

    insert_sql = "INSERT INTO sports_teams (team_id, league_id, name) VALUES (%s, %s, %s)"

    # 带有作用域约束 (league_id) 的查询与删除
    select_source_ids_sql = "SELECT team_id AS source_id FROM sports_teams WHERE league_id = %s AND status = 1"

    soft_delete_sql = "UPDATE sports_teams SET status = 0 WHERE team_id IN %s"

    delete_sql = "DELETE FROM sports_teams WHERE league_id = %s"

    def to_upsert_params(self, item: Team) -> Tuple:
        return (item.id, item.league_id, item.name)

    def to_insert_params(self, item: Team) -> Tuple:
        return (item.id, item.league_id, item.name)

    def get_entity_id(self, item: Team) -> str:
        return item.id