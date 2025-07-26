from rich.console import Console
from modules.Service.NaucniProgramService import NaucniProgramService
from modules.UI.BaseEntityUI import BaseEntityUI

class NaucniProgramUI(BaseEntityUI):
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