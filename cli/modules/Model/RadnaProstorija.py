from dataclasses import dataclass

@dataclass
class RadnaProstorija:
	id_rp: int
	naz: str
	lok: str
	tip: int
	id_prog: int