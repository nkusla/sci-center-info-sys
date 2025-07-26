from modules.DAO.BaseEntityDAO import BaseEntityDAO
from modules.Model.NaucniProgram import NaucniProgram

class NaucniProgramService:
	def __init__(self):
		self.dao = BaseEntityDAO('naucni_program', NaucniProgram)

	def get_all(self) -> list[NaucniProgram]:
		return self.dao.get_all()