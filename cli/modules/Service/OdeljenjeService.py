from modules.DAO.BaseEntityDAO import BaseEntityDAO

class OdeljenjeService:
	def __init__(self):
		self.dao = BaseEntityDAO('odeljenje')

	def get_all(self) -> list[tuple]:
		return self.dao.get_all()
