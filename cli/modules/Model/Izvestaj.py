from dataclasses import dataclass

@dataclass
class IzvestajOdeljenja:
	id_od: str
	naz: str
	sef: str
	broj_programa: int

@dataclass
class IzvestajRukovodjenja:
	id: int
	ime_prz: str
	naz: str
	id_od: str

@dataclass
class IzvestajPopisProstorija:
	id_prog: int
	naz: str
	br_kanc: int
	br_lab: int
	br_uci: int
