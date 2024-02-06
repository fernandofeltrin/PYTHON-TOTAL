import sqlite3

conexao = sqlite3.connect('base.db')

cursor = conexao.cursor()

cursor.execute("SELECT COUNT(*) FROM Usuarios")

total_registros = cursor.fetchone()[0]

print(f'Atualmente existe um total de {total_registros} registros na base de dados.')

conexao.close()
