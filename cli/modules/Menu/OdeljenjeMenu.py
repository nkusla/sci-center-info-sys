from rich.console import Console
from modules.Menu.BaseEntityMenu import BaseEntityMenu
from modules.Service.OdeljenjeService import OdeljenjeService

class OdeljenjeMenu(BaseEntityMenu):
	def __init__(self, console: Console):
		columns = ['ID', 'Naziv']

		super().__init__(
			console,
			OdeljenjeService(),
			'Odeljenja',
			columns
		)

	def show_all(self):
		super().show_all()