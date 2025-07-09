from modules.DAO.OsobaDAO import OsobaDAO

class OsobaService:
	def __init__(self):
		self.dao = OsobaDAO()

	def get_all(self) -> list[tuple]:
		return self.dao.get_all()

	def add_rukovodilac(self, osoba_id: int, program_id: int):
		if osoba_id == "" or program_id == "":
			raise ValueError("ID osobe i ID programa ne smeju biti prazni!")

		if not osoba_id.isdigit():
			raise ValueError("ID osobe mora biti broj!")

		self.dao.add_rukovodilac(osoba_id, program_id)
