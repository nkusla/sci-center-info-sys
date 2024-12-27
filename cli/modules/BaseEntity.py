from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from modules.utils import db_connect

class BaseEntity:
		def __init__(self, console: Console, table_name: str, table_title: str, columns: list):
			self.console = console
			self.table_name = table_name
			self.table_title = table_title
			self.columns = columns

		def show_all(self, attributes: list = None):
			with db_connect() as conn:
				table = Table(title=self.table_title, style="blue")
				for column in self.columns:
						table.add_column(column)

				table.columns[0].style = "green"

				if attributes is not None:
					query = f'SELECT {", ".join(attributes)} FROM {self.table_name}'
				else:
					query = f'SELECT * FROM {self.table_name}'

				cur = conn.cursor()
				cur.execute(query)
				for row in cur.fetchall():
						table.add_row(*[str(x) for x in row])
				self.console.print(table)
				Prompt.ask(">>")