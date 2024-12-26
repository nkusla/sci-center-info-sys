from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
from modules.utils import db_connect, clear_screen

class Izvestaj():
	def __init__(self, console: Console):
		self.console = console
		self.menu_options = "\n".join([
					"[1] Rukovodjenje programa",
					"[2] Izvestaj odelenja",
					"[3] ...",
					"[4] Nazad",
				])

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

			if choice == "1":
				self.izvestaj_rukovodjenja()
			elif choice == "2":
				self.izvestaj_odeljenja()
			elif choice == "4":
				break

	# Kompleksan upit
	def izvestaj_rukovodjenja(self):
		with db_connect() as con:
			cur = con.cursor()
			cur.execute('''
							SELECT np.id_np, np.naz
							FROM naucni_program np''')

			rows = cur.fetchall()

			table = Table(title="Izvestaj rukovodjenja")
			table.add_column("ID", style="green")
			table.add_column("Naziv naucnog programa")
			table.add_column("Ime")
			table.add_column("Prezime")

			for row in rows:
				table.add_row(*[str(x) for x in row])

			self.console.print(table)
			Prompt.ask(">>")

	# Kompleksan upit
	def izvestaj_odeljenja(self):
		with db_connect() as con:
			cur = con.cursor()
			cur.execute('''
							SELECT o.id_od, o.naz, COUNT(*) as br_naucnih_programa
							FROM odeljenje o
							LEFT JOIN naucni_program np ON o.id_od = np.id_od
							GROUP BY o.id_od, o.naz
							ORDER BY id_od;''')

			rows = cur.fetchall()

			table = Table(title="Izvestaj odeljenja")
			table.add_column("ID", style="green")
			table.add_column("Naziv")
			table.add_column("Broj naucnih programa")

			for row in rows:
				table.add_row(*[str(x) for x in row])

			self.console.print(table)
			Prompt.ask(">>")