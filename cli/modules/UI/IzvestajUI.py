from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
from modules.Service.IzvestajService import IzvestajService
from modules.utils import clear_screen, entity_to_list

class IzvestajUI:
	def __init__(self, console: Console):
		self.console = console
		self.service = IzvestajService()
		self.menu_options = "\n".join([
					"[1] Izvestaj odeljenja",
					"[2] Rukovodjenje programa",
					"[3] Popis prostorija",
					"[4] Nazad",
				])

		self.options = {}
		self.options["1"] = lambda: self.izvestaj_odeljenja()
		self.options["2"] = lambda: self.izvestaj_rukovodjenja()
		self.options["3"] = lambda: self.izvestaj_popis_prostorija()
		self.options["4"] = lambda: None

	def show_menu(self):
		while True:
			clear_screen()
			self.console.print(Panel.fit(
				self.menu_options,
				title="Izvestaji 📄",
				border_style="blue",
				padding=(1, 2)
			))
			choice = Prompt.ask(">>")
			clear_screen()

			if choice == "4":
				break

			if choice in self.options:
				self.options[choice]()

	# Kompleksan upit
	def izvestaj_odeljenja(self):
		entities = self.service.get_izvestaj_odeljenja()

		table = Table(title="Izvestaj odeljenja", style="blue")
		table.add_column("ID", style="green")
		table.add_column("Naziv")
		table.add_column("Sef odeljenja")
		table.add_column("Broj naucnih programa", justify="center")

		for entity in entities:
			table.add_row(*entity_to_list(entity))

		self.console.print(table)
		Prompt.ask(">>")

	# Kompleksan upit
	def izvestaj_rukovodjenja(self):
		entities = self.service.get_izvestaj_rukovodjenja()

		table = Table(title="Rukovodioci koji sami vode neki naucni program", style="blue")
		table.add_column("ID rukovodioca", style="green")
		table.add_column("Rukovodilac")
		table.add_column("Naziv programa")
		table.add_column("ID odeljenja")

		for entity in entities:
			table.add_row(*entity_to_list(entity))

		self.console.print(table)
		Prompt.ask(">>")

	# Jednostavan upit
	def izvestaj_popis_prostorija(self):
		entities = self.service.get_izvestaj_popis_prostorija()

		table = Table(title="Popis radnih prostorija po naucnim programima", style="blue")
		table.add_column("ID", style="green")
		table.add_column("Naziv programa")
		table.add_column("Broj kancelarija", justify="center")
		table.add_column("Broj laboratorija", justify="center")
		table.add_column("Broj ucionica", justify="center")

		for entity in entities:
			table.add_row(*entity_to_list(entity))

		self.console.print(table)
		Prompt.ask(">>")
