from modules.DAO.IzvestajDAO import IzvestajDAO

class IzvestajService:
	def __init__(self):
		self.dao = IzvestajDAO()

	def get_izvestaj_odeljenja(self) -> list[tuple]:
		return self.dao.get_izvestaj_odeljenja()

	def get_izvestaj_rukovodjenja(self) -> list[tuple]:
		return self.dao.get_izvestaj_rukovodjenja()

	def get_izvestaj_popis_prostorija(self) -> list[tuple]:
		return self.dao.get_izvestaj_popis_prostorija()
