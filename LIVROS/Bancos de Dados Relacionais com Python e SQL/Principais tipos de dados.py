import sqlite3

conexao = sqlite3.connect('base.db')

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estoque (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Item TEXT,
        Quantidade INTEGER,
        Valor REAL,
        Foto BLOB
    )
''')

conexao.commit()

conexao.close()
