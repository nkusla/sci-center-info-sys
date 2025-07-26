from rich.console import Console
from modules.UI.BaseEntityUI import BaseEntityUI
from modules.Service.OdeljenjeService import OdeljenjeService

class OdeljenjeUI(BaseEntityUI):
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