import sqlite3

# Conecta ao banco de dados (se não existir, o arquivo meubanco.db será criado)
try:
    with sqlite3.connect("meubanco.db") as banco:
        cursor = banco.cursor()

        # Cria a tabela de pessoas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
        """)

        # Dados de 7 pessoas para inserção
        pessoas = [
            ("Ana Silva", 28),
            ("Bruno Oliveira", 34),
            ("Carla Souza", 22),
            ("Daniel Mendes", 45),
            ("Eduardo Lima", 19),
            ("Fernanda Costa", 31),
            ("Gabriel Santos", 27)
        ]

        # Insere os registros na tabela
        cursor.executemany("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", pessoas)

        for amigos in pessoas:
            print(amigos)

        print("Banco de dados 'meubanco.db' criado e povoado com sucesso!")
except Exception as erro:
    print(f'Algo de errado: {erro}')

print('acabou')