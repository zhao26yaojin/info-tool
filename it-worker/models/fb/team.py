from dataclasses import dataclass

@dataclass(kw_only=True)
class Team:
	id: int = None

	name: str

	source_id: str

	logo: str

	tournament_name: str

	tournament_id: int = None

