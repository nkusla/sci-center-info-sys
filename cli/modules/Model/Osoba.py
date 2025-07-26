from dataclasses import dataclass

@dataclass
class Osoba:
	id: int
	jmbg: str
	ime: str
	prz: str
	br_tel: str
	email: str
	tip: str
	uloga: str