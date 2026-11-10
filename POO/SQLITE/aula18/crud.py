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

def cadastro_em_massa():
    cad_pessoas = {
        ("1", "Gustavo", "1.65"),
        ("2", "Ana", "1.45"),
        ("3", "João", "1.85"),
    }

    try: 
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.executemany("INSERT INTO pessoas (cod, nome, altura) VALUES (?, ?, ?)", cad_pessoas)
    except sqlite3.Error as erro:
        print('[ERRO] ao fazer cadastro em massa!')


def cadastro_pessoas() -> bool:
    print('=== NOVO CADASTRO DE PESSOA ===')

    # Leitura e validação dos dados
    val_nome = input("Nome: ").strip()

    if not val_nome:
        print("[ERRO] O nome é obrigatorio!")
        return False

    val_altura = input("Altura (metros): ").strip().replace(",", ".")

    if not val_altura:
        print("[ERRO] A altura é obrigatorio!")
        return False

    try:
        altura = float(val_altura)
        if altura <= 0.30 or altura > 3.0:
            print('[ERRO] Valor incorrente para altura!')
            return False
    except ValueError:
        print("[ERRO] A altura precisa ser um numero ")
        return False

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("INSERT INTO pessoas (nome, altura) VALUES (?, ?)", (val_nome, val_altura))

            print(f"Cadastro de {val_nome} realizado!")
            return True
    except sqlite3.Error as erro:
        print(f'[ERRO] Falha no cadastro do banco: {erro}')
        return False