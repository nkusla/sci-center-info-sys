from rich.console import Console
from modules.Service.RadnaProstorijaService import RadnaProstorijaService
from modules.Menu.BaseEntityMenu import BaseEntityMenu

class RadnaProstorijaMenu(BaseEntityMenu):
	def __init__(self, console: Console):
		columns = ['ID', 'Naziv', 'Lokacija', 'Tip', 'ID programa']

		super().__init__(
			console,
			RadnaProstorijaService(),
			'Radne prostorije',
			columns
		)

	def show_all(self):
		super().show_all()