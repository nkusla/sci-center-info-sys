from rich.console import Console
from modules.BaseEntity import BaseEntity

class Osoba(BaseEntity):
	def __init__(self, console: Console):
		columns = ['JMBG', 'Ime', 'Prezime', "Telefon", "Email", "Tip", "Saradnicka uloga"]
		super().__init__(console, 'osoba', 'Zaposleni, saradnici i polaznici centra', columns)

	def show_all(self):
		attributes = ['jmbg', 'ime', 'prz', 'br_tel', 'email', "tip", "uloga"]
		super().show_all(attributes)