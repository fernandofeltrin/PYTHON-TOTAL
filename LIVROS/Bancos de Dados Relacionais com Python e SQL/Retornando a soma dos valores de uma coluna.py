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

cursor.execute("SELECT SUM(Valor * Quantidade) FROM Inventario")

valor_total = cursor.fetchone()[0]

print(f'Inventário avaliado em R${valor_total}')

conexao.commit()

conexao.close()
