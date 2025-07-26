from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from modules.utils import db_connect
from typing import Type
from modules.utils import entity_to_row

class BaseEntityUI:
	def __init__(self, console: Console, service: Type, table_title: str, columns: list):
		self.console = console
		self.service = service
		self.table_title = table_title
		self.columns = columns

	def show_all(self):
		table = Table(title=self.table_title, style="blue")
		for column in self.columns:
				table.add_column(column)

		table.columns[0].style = "green"

		for entity in self.service.get_all():
			table.add_row(*entity_to_row(entity))

		self.console.print(table)
		Prompt.ask(">>")