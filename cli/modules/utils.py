import dataclasses
from typing import Type
import psycopg2
import os

DBNAME = 'sci_center'
HOST = '127.0.0.1'
USER = 'sci_center'
PASSWORD = 'sci_center'
PORT = "5434"

def db_connect():
	return psycopg2.connect(
		dbname=DBNAME,
		host=HOST,
		user=USER,
		password=PASSWORD,
		port=PORT
	)

def clear_screen():
	os.system('clear' if os.name == 'posix' else 'cls')

def entity_to_row(entity: list[Type]) -> list[str]:
	if not dataclasses.is_dataclass(entity):
		raise TypeError(f"{entity} is not a dataclass")

	return [str(getattr(entity, field.name)) for field in dataclasses.fields(entity)]
