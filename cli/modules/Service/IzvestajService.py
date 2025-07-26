from modules.DAO.IzvestajDAO import IzvestajDAO
from modules.Model.Izvestaj import *

class IzvestajService:
	def __init__(self):
		self.dao = IzvestajDAO()

	def get_izvestaj_odeljenja(self) -> list[IzvestajOdeljenja]:
		return self.dao.get_izvestaj_odeljenja()

	def get_izvestaj_rukovodjenja(self) -> list[IzvestajRukovodjenja]:
		return self.dao.get_izvestaj_rukovodjenja()

	def get_izvestaj_popis_prostorija(self) -> list[IzvestajPopisProstorija]:
		return self.dao.get_izvestaj_popis_prostorija()
