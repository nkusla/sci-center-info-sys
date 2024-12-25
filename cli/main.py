from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
import os
from connection import connect

console = Console()

def clear_screen():
  os.system('clear' if os.name == 'posix' else 'cls')

def glavni_meni(console):
    console.print(Panel.fit(
        "\n".join([
            "[1] Odeljenja",
            "[2] Naucni programi",
            "[3] Radne prostorije",
            "[5] Izlaz"
        ]),
        title="Naucni centar",
        border_style="blue"
    ))
    return Prompt.ask(">>")

def prikazi_naucne_programe(console):
	with connect() as conn:
		table = Table(title="Naucni programi")
		table.add_column("ID", style="green")
		table.add_column("Naziv")
		table.add_column("Odeljenje")

		cur = conn.cursor()
		cur.execute('SELECT * FROM naucni_program')
		for row in cur.fetchall():
				table.add_row(*[str(x) for x in row])
		console.print(table)

		Prompt.ask(">>")

def prikazi_odeljenja(console):
	with connect() as conn:
		table = Table(title="Odeljenja")
		table.add_column("ID", style="green")
		table.add_column("Naziv")

		cur = conn.cursor()
		cur.execute('SELECT * FROM odeljenje')
		for row in cur.fetchall():
				table.add_row(*[str(x) for x in row])
		console.print(table)

		Prompt.ask(">>")

def prikazi_radne_prostorije(console):
	with connect() as conn:
		table = Table(title="Radne prostorije")
		table.add_column("ID", style="green")
		table.add_column("Naziv")
		table.add_column("Lokacija")
		table.add_column("Tip")
		table.add_column("ID program")

		cur = conn.cursor()
		cur.execute('SELECT * FROM radna_prostorija')
		for row in cur.fetchall():
				table.add_row(*[str(x) for x in row])
		console.print(table)

		Prompt.ask(">>")

def main():
	while True:
		clear_screen()
		choice = glavni_meni(console)
		clear_screen()
		if choice == "1":
			prikazi_naucne_programe(console)
		elif choice == "2":
			prikazi_odeljenja(console)
		elif choice == "3":
			prikazi_radne_prostorije(console)
		elif choice == "5":
			break

if __name__ == '__main__':
    main()