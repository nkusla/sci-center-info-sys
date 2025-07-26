from modules.DAO.BaseEntityDAO import BaseEntityDAO
from modules.Model.RadnaProstorija import RadnaProstorija

class RadnaProstorijaService:
	def __init__(self):
		self.dao = BaseEntityDAO('radna_prostorija', RadnaProstorija)

	def get_all(self) -> list[RadnaProstorija]:
		return self.dao.get_all()