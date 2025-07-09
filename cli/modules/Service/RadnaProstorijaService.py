from modules.DAO.BaseEntityDAO import BaseEntityDAO

class RadnaProstorijaService:
	def __init__(self):
		self.dao = BaseEntityDAO('radna_prostorija')

	def get_all(self) -> list[tuple]:
		return self.dao.get_all()