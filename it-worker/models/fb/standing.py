from dataclasses import dataclass

@dataclass
class Standing:
	id: int

	name: str

	tournament_name: str

	tournament_id: int

	source_id: str

	wins: int

	draws: int

	losses: int

	goals_for: int

	goals_against: int

	goal_difference: int

	points: int

