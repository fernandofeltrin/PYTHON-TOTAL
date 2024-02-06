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

dados = {'Itens': ['Tênis Nike', 'Camisa Adidas GG', 'Bermuda Umbro', 'Camisa Adidas P'],
         'Quantidade': [5, 4, 1, 2],
         'Valor': [149.90, 99.90, 69.90, 79.90]}

dados = list(zip(dados['Itens'], dados['Quantidade'], dados['Valor']))

cursor.executemany("INSERT INTO Inventario (Item, Quantidade, Valor) VALUES (?, ?, ?)", dados)

cursor.execute("SELECT MAX(Valor) FROM Inventario")

valor_maximo = cursor.fetchone()[0]

cursor.execute("SELECT MIN(Valor) FROM Inventario")

valor_minimo = cursor.fetchone()[0]

print(f'Valor máximo encontrado: R${valor_maximo:.2f}'
      f'\nValor mínimo encontrado: R${valor_minimo:.2f}')

conexao.commit()

conexao.close()
