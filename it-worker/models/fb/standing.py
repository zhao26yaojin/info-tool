from dataclasses import dataclass

@dataclass(kw_only=True)
class Standing:
	id: int = None

	team_name: str

	team_id: int = None

	tournament_name: str

	tournament_id: int = None

	source_id: str

	wins: int

	draws: int

	losses: int

	goals_for: int

	goals_against: int

	goal_difference: int

	points: int

