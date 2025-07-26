from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from modules.UI.NaucniProgramUI import NaucniProgramUI
from modules.UI.OdeljenjeUI import OdeljenjeUI
from modules.UI.RadnaProstorijaUI import RadnaProstorijaUI
from modules.UI.IzvestajUI import IzvestajUI
from modules.UI.OsobaUI import OsobaUI
from modules.utils import clear_screen

banner = '''[bold blue]
 _   _                        _                  _
| \ | | __ _ _   _  ___ _ __ (_)   ___ ___ _ __ | |_ __ _ _ __
|  \| |/ _` | | | |/ __| '_ \| |  / __/ _ \ '_ \| __/ _` | '__|
| |\  | (_| | |_| | (__| | | | | | (_|  __/ | | | || (_| | |
|_| \_|\__,_|\__,_|\___|_| |_|_|  \___\___|_| |_|\__\__,_|_|   '''

class MainUI():
	def __init__(self):
		self.console = Console()
		self.options = {}
		self.menu_options = "\n".join([
			"[1] Odeljenja",
			"[2] Naucni programi",
			"[3] Radne prostorije",
			"[4] Osobe u centru",
			"[5] Izvestaji",
			"[6] Izlaz"
		])

		naucni_program = NaucniProgramUI(self.console)
		odeljenje = OdeljenjeUI(self.console)
		radna_prostorija = RadnaProstorijaUI(self.console)
		izvestaj = IzvestajUI(self.console)
		osoba = OsobaUI(self.console)

		self.options["1"] = lambda: odeljenje.show_all()
		self.options["2"] = lambda: naucni_program.show_all()
		self.options["3"] = lambda: radna_prostorija.show_all()
		self.options["4"] = lambda: osoba.run()
		self.options["5"] = lambda: izvestaj.show_menu()
		self.options["6"] = lambda: exit()

	def show_menu(self):
		self.console.print(banner)
		self.console.print(Panel.fit(
			self.menu_options,
			border_style="blue",
			padding=(1, 6)
		))
		return Prompt.ask(">>")

	def run(self):
		while True:
			clear_screen()
			choice = self.show_menu()
			clear_screen()

			if choice in self.options:
				self.options[choice]()
