from modules.DAO.BaseEntityDAO import BaseEntityDAO

class NaucniProgramService:
	def __init__(self):
		self.dao = BaseEntityDAO('naucni_program')

	def get_all(self) -> list[tuple]:
		return self.dao.get_all()