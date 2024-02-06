import sqlite3

conexao = sqlite3.connect('base.db')

cursor = conexao.cursor()

cursor.execute("INSERT INTO Usuarios (Nome, Email, Profissão) VALUES (?, ?, ?)",
               ('João da Silva', 'joao_silva@gmail.com', 'Arquiteto'))

conexao.commit()

conexao.close()
