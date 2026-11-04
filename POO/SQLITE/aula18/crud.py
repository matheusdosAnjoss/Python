import sqlite3

NOME_BANCO = 'cadastro.db'

def criar_banco() -> bool:
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (cod INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, altura REAL NOT NULL)")
        return True 
    except sqlite3.Error as erro:
        print(f'Falha na criação do banco: {erro}')
        return False