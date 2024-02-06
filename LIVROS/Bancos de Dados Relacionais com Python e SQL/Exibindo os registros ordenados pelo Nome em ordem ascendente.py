import sqlite3

conexao = sqlite3.connect('base.db')

cursor = conexao.cursor()

#cursor.execute("SELECT * FROM Usuarios")
cursor.execute("SELECT * FROM Usuarios ORDER BY Nome ASC")

print(f'Usuários organizados por nome em ordem alfabética:')
for i in cursor.fetchall():
    print(f'Nome: {i[1]}, E-mail: {i[2] if i[2] is not None else ""}, Telefone: {i[3] if i[3] is not None else ""}, Profissão: {i[4] if i[4] is not None else ""}')

#conexao.commit() Como não foi realizada nenhuma alteração na base de dados, não se faz necessário aplicar o método commit()

conexao.close()
