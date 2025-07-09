from rich.console import Console
from modules.Service.NaucniProgramService import NaucniProgramService
from modules.Menu.BaseEntityMenu import BaseEntityMenu

class NaucniProgramMenu(BaseEntityMenu):
	def __init__(self, console: Console):
		columns = ['ID', 'Naziv', 'Odeljenje']

		super().__init__(
			console,
			NaucniProgramService(),
			'Naucni programi',
			columns
		)

	def show_all(self):
		super().show_all()