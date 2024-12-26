from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
import os
from modules.NaucniProgram import NaucniProgram
from modules.Odeljenje import Odeljenje
from modules.RadnaProstorija import RadnaProstorija

class MainMenu():
	def __init__(self):
		self.console = Console()
		self.options = {}

		naucni_program = NaucniProgram(self.console)
		odeljenje = Odeljenje(self.console)
		radna_prostorija = RadnaProstorija(self.console)

		self.options["1"] = lambda: odeljenje.show_all()
		self.options["2"] = lambda: naucni_program.show_all()
		self.options["3"] = lambda: exit()
		self.options["4"] = lambda: radna_prostorija.show_all()
		self.options["5"] = lambda: exit()

	def clear_screen(self):
		os.system('clear' if os.name == 'posix' else 'cls')

	def show_menu(self):
		self.console.print(Panel.fit(
			"\n".join([
				"[1] Odeljenja",
				"[2] Naucni programi",
				"[3] Seminari",
				"[4] Radne prostorije",
				"[5] Izlaz"
			]),
			title="Naucno-istrazivacki centar",
			border_style="blue"
		))
		return Prompt.ask(">>")

	def run(self):
		while True:
			self.clear_screen()
			choice = self.show_menu()
			self.clear_screen()

			if choice in self.options:
				self.options[choice]()
