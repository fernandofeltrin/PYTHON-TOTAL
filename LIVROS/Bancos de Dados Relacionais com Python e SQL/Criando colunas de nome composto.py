import sqlite3

conexao = sqlite3.connect('base.db')

cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Email TEXT,
        'Num Telefone' TEXT
    )
""")

conexao.commit()

conexao.close()
