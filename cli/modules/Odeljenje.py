from rich.console import Console
from modules.BaseEntity import BaseEntity

class Odeljenje(BaseEntity):
	def __init__(self, console: Console):
		columns = ['ID', 'Naziv']
		super().__init__(console, 'odeljenje', 'Odeljenja', columns)

	def show_all(self):
		super().show_all()