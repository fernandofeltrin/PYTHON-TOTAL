import sqlite3

conexao = sqlite3.connect('base.db')

cursor = conexao.cursor()

cursor.execute("PRAGMA table_info(Usuarios)")
colunas = cursor.fetchall()

print("Informações sobre as colunas da tabela 'Usuarios':")
for i in colunas:
    print(f"Nome da coluna: {i[1]}, Tipo de dado esperado: {i[2]}, Pode ser Nulo: {'Sim' if i[3] == 1 else 'Não'}")

conexao.close()
