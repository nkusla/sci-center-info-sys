from modules.Model.Odeljenje import Odeljenje
from modules.DAO.BaseEntityDAO import BaseEntityDAO

class OdeljenjeService:
	def __init__(self):
		self.dao = BaseEntityDAO('odeljenje', Odeljenje)

	def get_all(self) -> list[Odeljenje]:
		return self.dao.get_all()
