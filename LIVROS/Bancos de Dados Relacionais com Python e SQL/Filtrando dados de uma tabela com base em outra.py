import sqlite3

conexao = sqlite3.connect('base.db')

cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY,
        Nome TEXT,
        Telefone INTEGER )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pedidos (
        id INTEGER PRIMARY KEY,
        id_Cliente INTEGER,
        Item TEXT,
        Qtd INTEGER,
        FOREIGN KEY (id_Cliente) REFERENCES Clientes (id) )
""")

conexao.commit()

cursor.execute("INSERT INTO Clientes (Nome, Telefone) VALUES (?, ?)", ('João', 51984175670))
cursor.execute("INSERT INTO Clientes (Nome, Telefone) VALUES (?, ?)", ('Maria', 11956501129))

cursor.execute("INSERT INTO Pedidos (id_Cliente, Item, Qtd) VALUES (?, ?, ?)", (1, 'Tênis', 2))
cursor.execute("INSERT INTO Pedidos (id_Cliente, Item, Qtd) VALUES (?, ?, ?)", (1, 'Camiseta', 3))
cursor.execute("INSERT INTO Pedidos (id_Cliente, Item, Qtd) VALUES (?, ?, ?)", (2, 'Shorts', 1))

conexao.commit()

cursor.execute("""
    SELECT Clientes.id AS cliente_id, Clientes.Nome AS cliente_nome, Pedidos.Item, Pedidos.Qtd
    FROM Clientes
    LEFT JOIN Pedidos ON Clientes.id = Pedidos.id_Cliente
""")

for i in cursor.fetchall():
    print(f'Id: {i[0]}, Cliente: {i[1]}, Item: {i[2]}, Quantidade: {i[3]}')

conexao.close()
