from rich.console import Console
from modules.Menu.BaseEntityMenu import BaseEntityMenu

class OdeljenjeMenu(BaseEntityMenu):
	def __init__(self, console: Console):
		self.columns = ['ID', 'Naziv']
		self.console = console
		super().__init__(console, 'odeljenje', 'Odeljenja', self.columns)

	def show_all(self):
		super().show_all()