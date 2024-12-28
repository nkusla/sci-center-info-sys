from rich.console import Console
from modules.BaseEntity import BaseEntity

class Odeljenje(BaseEntity):
	def __init__(self, console: Console):
		self.columns = ['ID', 'Naziv']
		self.console = console
		super().__init__(console, 'odeljenje', 'Odeljenja', self.columns)

	def show_all(self):
		super().show_all()