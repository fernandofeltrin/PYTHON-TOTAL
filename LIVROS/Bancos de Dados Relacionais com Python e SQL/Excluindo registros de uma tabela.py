import sqlite3

nome = input('Digite um nome a ser excluído: ').capitalize()

conexao = sqlite3.connect('base.db')

cursor = conexao.cursor()

cursor.execute("DELETE FROM Usuarios WHERE Nome = ?", nome)

cursor.execute("SELECT * FROM Usuarios")

for i in cursor.fetchall():
    print(f'Nome: {i[1]}, E-mail: {i[2] if i[2] is not None else ""}, Telefone: {i[3] if i[3] is not None else ""}, Profissão: {i[4] if i[4] is not None else ""}')

conexao.commit()

conexao.close()
