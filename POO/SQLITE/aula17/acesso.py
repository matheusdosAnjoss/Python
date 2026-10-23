import sqlite3
from datetime import datetime, date

busca = str(input("Quem você está procurando? ")).strip()
while not busca:
    print("A busca não pode ser vazia! Digite um nome.")
    busca = str(input("Quem você está procurando? ")).strip()

try:
    with sqlite3.connect("meubanco.db") as banco:
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM pessoas_detalhado WHERE nome LIKE ?", (f"%{busca}%",))

        total = 0
        hoje = date.today()
        for total, pessoa in enumerate(cursor , start=1):
            # print(f'{pessoa[1]} {pessoa[2]} nasceu em {pessoa[3]}')
            data_nasc = datetime.strptime(pessoa[3], "%Y-%m-%d").date()

            idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

            data_formatada = data_nasc.strftime("%d/%m/%Y")

            print(f'{pessoa[1]} {pessoa[2]} nasceu em {data_formatada} e tem {idade} anos.')

        if total == 0:
            print(f"Nenhum registro foi encontrado com o nome '{busca}' ")
        else:
            termo = "pessoa" if total == 1 else "pessoas"
            print(f"Ao todo encontrei {total} {termo} com '{busca}'")

except sqlite3.Error as erro:
    print(f'Falha no banco: {erro}')

except Exception as erro:
    print(f'Algo de errado: {erro}')
