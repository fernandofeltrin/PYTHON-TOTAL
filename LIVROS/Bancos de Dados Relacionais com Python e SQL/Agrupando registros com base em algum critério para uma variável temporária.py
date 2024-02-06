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

cursor.execute("""
    SELECT SUM(Quantidade) AS quantidade_total, SUM(Valor * Quantidade) AS valor_total
    FROM Inventario
    WHERE Item LIKE 'Camisa%'
""")

resultado = cursor.fetchone()

if resultado:
    quantidade_total, valor_total = resultado
    print(f'Total de camisas da marca Adidas: {quantidade_total}'
          f'\nValor Total: R${valor_total:.2f}')
else:
    print("Nenhuma camisa encontrada no inventário.")

conexao.commit()

conexao.close()
