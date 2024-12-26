from rich.console import Console
from modules.BaseEntity import BaseEntity

class RadnaProstorija(BaseEntity):
	def __init__(self, console: Console):
		columns = ['ID', 'Naziv', 'Lokacija', 'Tip', 'ID programa']
		super().__init__(console, 'radna_prostorija', 'Radne prostorije', columns)

	def show_all(self):
		super().show_all()