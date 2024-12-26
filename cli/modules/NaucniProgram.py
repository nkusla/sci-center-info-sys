from rich.console import Console
from modules.BaseEntity import BaseEntity

class NaucniProgram(BaseEntity):
	def __init__(self, console: Console):
		columns = ['ID', 'Naziv', 'Odeljenje']
		super().__init__(console, 'naucni_program', 'Naucni programi', columns)

	def show_all(self):
		super().show_all()