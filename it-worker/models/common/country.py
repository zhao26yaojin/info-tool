from dataclasses import dataclass

@dataclass(kw_only=True)
class Country:
	id: int = None

	name: str

	logo: str

	source_id: str

	region: str

