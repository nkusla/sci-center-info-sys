import psycopg2
import os

DBNAME = 'sci_center'
HOST = '127.0.0.1'
USER = 'sci_center'
PASSWORD = 'sci_center'
PORT = "5434"

def db_connect():
	return psycopg2.connect(
		dbname=DBNAME,
		host=HOST,
		user=USER,
		password=PASSWORD,
		port=PORT
	)

def clear_screen():
	os.system('clear' if os.name == 'posix' else 'cls')