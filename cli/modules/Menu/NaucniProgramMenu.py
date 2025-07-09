from rich.console import Console
from modules.Menu.BaseEntityMenu import BaseEntityMenu

class NaucniProgramMenu(BaseEntityMenu):
	def __init__(self, console: Console):
		self.columns = ['ID', 'Naziv', 'Odeljenje']
		super().__init__(console, 'naucni_program', 'Naucni programi', self.columns)

	def show_all(self):
		super().show_all()