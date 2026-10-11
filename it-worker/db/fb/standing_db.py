from db.db_base import DbBase
from models.fb.standing import Standing

class StandingDb(DbBase[Standing]):
	upsert_sql: str = """
        INSERT INTO fb_standing (id, team_id, tournament_id, source_id, wins, draws, losses, goals_for, goals_against, goal_difference, points)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) AS new
        ON DUPLICATE KEY UPDATE
            team_id = new.team_id,
			tournament_id = new.tournament_id,
			wins = new.wins,
			draws = new.draws,
			losses = new.losses,
			goals_for = new.goals_for,
			goals_against = new.goals_against,
			goal_difference = new.goal_difference,
			points = new.points;
    """

	insert_sql: str = """
            INSERT INTO fb_standing (id, team_id, tournament_id, source_id, wins, draws, losses, goals_for, goals_against, goal_difference, points)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

	select_batch_source_ids_sql: str = """
            SELECT source_id
            FROM fb_standing
            WHERE tournament_id = %s
        """

	delete_sql: str = """
            DELETE FROM fb_standing
            WHERE source_id IN %s
        """

	def to_upsert_params(self, item: Standing):
		return item.id, item.team_id, item.tournament_id, item.source_id, item.wins, item.draws, item.losses, item.goals_for, item.goals_against, item.goal_difference, item.points

	def to_insert_params(self, item: Standing):
		return item.id, item.team_id, item.tournament_id, item.source_id, item.wins, item.draws, item.losses, item.goals_for, item.goals_against, item.goal_difference, item.points

