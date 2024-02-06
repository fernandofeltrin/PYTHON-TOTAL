import sqlite3

conexao = sqlite3.connect('base.db')

cursor = conexao.cursor()

cursor.execute("INSERT INTO Usuarios (Nome, Email, Profissão) VALUES (?, ?, ?)",
               ('João da Silva', 'joao_silva@gmail.com', 'Arquiteto'))

cursor.execute("SELECT * FROM Usuarios")

for i in cursor.fetchall():
    print(f'Nome: {i[1]}, E-mail: {i[2] if i[2] is not None else ""}, Telefone: {i[3] if i[3] is not None else ""}, Profissão: {i[4] if i[4] is not None else ""}')

conexao.commit()

conexao.close()
