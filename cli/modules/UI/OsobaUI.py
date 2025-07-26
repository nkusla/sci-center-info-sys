from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from modules.Service.OsobaService import OsobaService
from modules.UI.BaseEntityUI import BaseEntityUI
from modules.utils import clear_screen, db_connect

class OsobaUI(BaseEntityUI):
	def __init__(self, console: Console):
		columns = ['ID', 'JMBG', 'Ime', 'Prezime', "Telefon", "Email", "Tip", "Saradnicka uloga"]
		super().__init__(
			console,
			OsobaService(),
			'Zaposleni, saradnici i polaznici centra',
			columns
		)

		self.menu_options = "\n".join([
			"[1] Prikazi sve",
			"[2] Dodavanje rukovodioca programu",
			"[3] Nazad"
		])

		self.options = {}
		self.options["1"] = lambda: self.show_all()
		self.options["2"] = lambda: self.add_rukovodilac()
		self.options["3"] = lambda: None

	def show_menu(self):
		self.console.print(Panel.fit(
			self.menu_options,
			title="Osobe u centru",
			border_style="blue",
			padding=(1, 6)
		))
		return Prompt.ask(">>")

	def run(self):
		while True:
			clear_screen()
			choice = self.show_menu()
			clear_screen()

			if choice == "3":
				break

			if choice in self.options:
				self.options[choice]()

	def add_rukovodilac(self):
		with db_connect() as conn:
			try:
				self.console.print("Posavljanje rukovodioca programa\n", style="bold blue")
				osoba_id = Prompt.ask("Unesite ID osobe")
				program_id = Prompt.ask("Unesite ID programa")

				self.service.add_rukovodilac(osoba_id, program_id)

				self.console.print(f"[green]Uspesno dodat rukovodilac programa {program_id}")
			except Exception as e:
				self.console.print(f"[red]Greska: {e}")

		return Prompt.ask(">>")