from modules.utils import db_connect
from modules.DAO.BaseEntityDAO import BaseEntityDAO
from modules.Model.Osoba import Osoba

class OsobaDAO(BaseEntityDAO):
	def __init__(self):
		super().__init__('osoba', Osoba)

	def add_rukovodilac(self, osoba_id: int, program_id: int):
		with db_connect() as conn:
			try:
				cur = conn.cursor()
				cur.execute(f"SELECT * FROM osoba WHERE id = %s AND tip = 'SARADNIK'", (osoba_id,))
				if cur.rowcount == 0:
					raise Exception("Osoba sa unetim ID-jem ne postoji ili nije saradnik centra!")

				cur.execute(f"SELECT * FROM naucni_program WHERE id_prog = %s", (program_id,))
				if cur.rowcount == 0:
					raise Exception("Naucni program sa unetim ID-jem ne postoji!")

				cur.execute(f"UPDATE osoba SET uloga = 'RUKOVODILAC' WHERE id = %s AND tip = 'SARADNIK'", (osoba_id,))
				cur.execute(f"INSERT INTO rukovodi (osoba_id, id_prog) VALUES (%s, %s)", (osoba_id, program_id))

				conn.commit()
			except Exception as e:
				conn.rollback()
				raise e
