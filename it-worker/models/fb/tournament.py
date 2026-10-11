from dataclasses import dataclass

@dataclass(kw_only=True)
class Tournament:
	id: int = None

	name: str

	source_id: str

	logo: str

