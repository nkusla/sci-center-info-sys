from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from modules.BaseEntity import BaseEntity
from modules.utils import clear_screen, db_connect

class Osoba(BaseEntity):
	def __init__(self, console: Console):
		self.columns = ['ID', 'JMBG', 'Ime', 'Prezime', "Telefon", "Email", "Tip", "Saradnicka uloga"]
		self.console = console
		super().__init__(console, 'osoba', 'Zaposleni, saradnici i polaznici centra', self.columns)

		self.options = {}
		self.menu_options = "\n".join([
			"[1] Prikazi sve",
			"[2] Dodavanje rukovodioca programu",
			"[3] Nazad"
		])

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

				if osoba_id == "" or program_id == "":
					return

				if not osoba_id.isdigit():
					raise Exception("ID osobe mora biti broj!")

				cur = conn.cursor()
				cur.execute(f"SELECT * FROM osoba WHERE id = %s AND tip = 'SARADNIK'", (osoba_id,))
				if cur.rowcount == 0:
					raise Exception("Osoba sa unetim ID-jem ne postoji ili nije saradnik centra!")

				cur.execute(f"UPDATE osoba SET uloga = 'RUKOVODILAC' WHERE id = %s AND tip = 'SARADNIK'", (osoba_id,))
				cur.execute(f"INSERT INTO rukovodi (osoba_id, id_prog) VALUES (%s, %s)", (osoba_id, program_id))

				conn.commit()
				self.console.print(f"[green]Uspesno dodat rukovodilac programa {program_id}")
			except Exception as e:
				conn.rollback()
				self.console.print(f"[red]Greska: {e}")

		return Prompt.ask(">>")

	def show_all(self):
		attributes = ['id', 'jmbg', 'ime', 'prz', 'br_tel', 'email', "tip", "uloga"]
		super().show_all(attributes)