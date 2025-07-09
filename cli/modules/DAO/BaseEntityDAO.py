from modules.utils import db_connect

class BaseEntityDAO:
	def __init__(self, table_name: str, attributes: list[str] = None):
		self.table_name = table_name
		self.attributes = attributes

	def get_all(self) -> list[tuple]:
		with db_connect() as conn:
			if self.attributes is not None:
				query = f'SELECT {", ".join(self.attributes)} FROM {self.table_name}'
			else:
				query = f'SELECT * FROM {self.table_name}'

			cur = conn.cursor()
			cur.execute(query)
			return cur.fetchall()