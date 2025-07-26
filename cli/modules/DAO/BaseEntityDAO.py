from modules.utils import db_connect
from typing import Type
import dataclasses

class BaseEntityDAO:
	def __init__(self, table_name: str, entity_type: Type):
		self.table_name = table_name
		self.entity_type = entity_type

	def get_all(self) -> list[Type]:
		with db_connect() as conn:
			if not dataclasses.is_dataclass(self.entity_type):
				raise TypeError(f"{self.entity_type} is not a dataclass")

			field_names = [field.name for field in dataclasses.fields(self.entity_type)]
			query = f'SELECT {", ".join(field_names)} FROM {self.table_name}'

			cur = conn.cursor()
			cur.execute(query)

			entities = [self.entity_type(*row) for row in cur.fetchall()]
			return entities