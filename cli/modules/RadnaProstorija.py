from rich.console import Console
from modules.BaseEntity import BaseEntity

class RadnaProstorija(BaseEntity):
	def __init__(self, console: Console):
		self.columns = ['ID', 'Naziv', 'Lokacija', 'Tip', 'ID programa']
		self.console = console
		super().__init__(console, 'radna_prostorija', 'Radne prostorije', self.columns)

	def show_all(self):
		super().show_all()