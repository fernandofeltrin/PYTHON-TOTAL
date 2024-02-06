import sqlite3

conexao = sqlite3.connect('base.db')

cursor = conexao.cursor()

dados = {'Nome': ['Patricia Souza', 'Paulo Marques'],
         'Email': ['paty_souza@outlook.com', 'p.marques1970@gmail.com']}

for i in range(len(dados['Nome'])):
    registros = [dados[chave][i] for chave in dados.keys()]
    cursor.execute("INSERT INTO Usuarios (Nome, Email) VALUES (:Nome, :Email)", registros)

cursor.execute("SELECT * FROM Usuarios")

for i in cursor.fetchall():
    print(f'Nome: {i[1]}, E-mail: {i[2] if i[2] is not None else ""}, Telefone: {i[3] if i[3] is not None else ""}, Profissão: {i[4] if i[4] is not None else ""}')

conexao.commit()

conexao.close()

///


import sqlite3

conexao = sqlite3.connect('base.db')

cursor = conexao.cursor()

dados = {'Nome': ['Patricia Souza', 'Paulo Marques'],
         'Email': ['paty_souza@outlook.com', 'p.marques1970@gmail.com']}

dados = list(dados)

cursor.execute("INSERT INTO Usuarios (Nome, Email) VALUES (:Nome, :Email)", dados)

cursor.execute("SELECT * FROM Usuarios")

for i in cursor.fetchall():
    print(f'Nome: {i[1]}, E-mail: {i[2] if i[2] is not None else ""}, Telefone: {i[3] if i[3] is not None else ""}, Profissão: {i[4] if i[4] is not None else ""}')

conexao.commit()

conexao.close()
