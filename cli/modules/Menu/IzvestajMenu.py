from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
from modules.utils import db_connect, clear_screen

class IzvestajMenu():
	def __init__(self, console: Console):
		self.console = console
		self.menu_options = "\n".join([
					"[1] Izvestaj odeljenja",
					"[2] Rukovodjenje programa",
					"[3] Popis prostorija",
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
				self.izvestaj_odeljenja()
			elif choice == "2":
				self.izvestaj_rukovodjenja()
			elif choice == "3":
				self.izvestaj_popis_prostorija()
			elif choice == "4":
				break

	# Kompleksan upit
	def izvestaj_odeljenja(self):
		with db_connect() as con:
			cur = con.cursor()
			cur.execute('''
				WITH odeljenja_stats AS (
					SELECT o.id_od, o.naz, COUNT(np.id_od) AS broj_programa
					FROM odeljenje o
					LEFT OUTER JOIN naucni_program np ON o.id_od = np.id_od
					GROUP BY o.id_od, o.naz
					ORDER BY id_od
				),
				sefovi_odeljenja AS (
					SELECT CONCAT(o.ime, ' ', o.prz) AS sef, od.id_od
					FROM osoba o
					INNER JOIN rukovodi r ON o.id = r.osoba_id
					INNER JOIN naucni_program np ON r.id_prog = np.id_prog
					INNER JOIN odeljenje od ON np.id_od = od.id_od
					WHERE r.upr = TRUE
				)
				SELECT os.id_od, os.naz, COALESCE(so.sef, 'NEMA') AS sef, os.broj_programa
				FROM odeljenja_stats os
				LEFT OUTER JOIN sefovi_odeljenja so ON os.id_od = so.id_od;
			''')

			rows = cur.fetchall()

			table = Table(title="Izvestaj odeljenja", style="blue")
			table.add_column("ID", style="green")
			table.add_column("Naziv")
			table.add_column("Sef odeljenja")
			table.add_column("Broj naucnih programa", justify="center")

			for row in rows:
				table.add_row(*[str(x) for x in row])

			self.console.print(table)
			Prompt.ask(">>")

	# Kompleksan upit
	def izvestaj_rukovodjenja(self):
		with db_connect() as con:
			cur = con.cursor()
			cur.execute('''
				WITH sami_programi AS (
					SELECT id_prog
					FROM rukovodi
					GROUP BY id_prog
					HAVING COUNT(id_prog) = 1
				),
				rukovodici AS (
					SELECT o.id, o.ime, o.prz
					FROM osoba o
					WHERE o.uloga = 'RUKOVODILAC'
				)
				SELECT ruk.id, CONCAT(ruk.ime, ' ', ruk.prz), np.naz, COALESCE(np.id_od, 'NEMA')
				FROM rukovodici ruk
				INNER JOIN rukovodi r ON ruk.id = r.osoba_id
				RIGHT JOIN sami_programi sp ON r.id_prog = sp.id_prog
				LEFT JOIN naucni_program np ON sp.id_prog = np.id_prog
				ORDER BY ruk.ime, ruk.prz;
			''')

			rows = cur.fetchall()

			table = Table(title="Rukovodioci koji sami vode neki naucni program", style="blue")
			table.add_column("ID rukovodioca", style="green")
			table.add_column("Rukovodilac")
			table.add_column("Naziv programa")
			table.add_column("ID odeljenja")

			for row in rows:
				table.add_row(*[str(x) for x in row])

			self.console.print(table)
			Prompt.ask(">>")

	# Jednostavan upit
	def izvestaj_popis_prostorija(self):
		with db_connect() as con:
			cur = con.cursor()
			cur.execute('''
				SELECT
						np.id_prog,
						np.naz,
						COUNT(CASE WHEN tip = 'KANC' THEN 1 END) as br_kanc,
						COUNT(CASE WHEN tip = 'LAB' THEN 1 END) as br_lab,
						COUNT(CASE WHEN tip = 'UCIONICA' THEN 1 END) as br_uci
				FROM radna_prostorija rp
				RIGHT JOIN naucni_program np ON np.id_prog = rp.id_prog
				GROUP BY np.id_prog
				ORDER BY np.id_prog;
			''')

			rows = cur.fetchall()

			table = Table(title="Popis radnih prostorija po naucnim programima", style="blue")
			table.add_column("ID", style="green")
			table.add_column("Naziv programa")
			table.add_column("Broj kancelarija", justify="center")
			table.add_column("Broj laboratorija", justify="center")
			table.add_column("Broj ucionica", justify="center")

			for row in rows:
				table.add_row(*[str(x) for x in row])

			self.console.print(table)
			Prompt.ask(">>")
