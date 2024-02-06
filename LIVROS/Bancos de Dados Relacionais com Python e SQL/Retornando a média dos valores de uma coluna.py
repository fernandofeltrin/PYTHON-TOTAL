import sqlite3

conexao = sqlite3.connect('base.db')

cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Inventario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Item TEXT,
        Quantidade INTEGER,
        Valor REAL
    )
""")

dados = {'Itens': ['Tênis Nike', 'Camisa Adidas', 'Bermuda Umbro'],
         'Quantidade': [5, 4, 1],
         'Valor': [149.90, 99.90, 69.90]}

dados = list(zip(dados['Itens'], dados['Quantidade'], dados['Valor']))

cursor.executemany("INSERT INTO Inventario (Item, Quantidade, Valor) VALUES (?, ?, ?)", dados)

cursor.execute("SELECT AVG(Valor) FROM Inventario")

valor_total = cursor.fetchone()[0]

print(f'Valor médio dos itens do inventário: R${valor_total:.2f}')

conexao.commit()

conexao.close()
