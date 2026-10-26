import sqlite3
from datetime import datetime, date

busca = str(input("Quem você está procurando? ")).strip()
while not busca:
    print("A busca não pode ser vazia! Digite um nome.")
    busca = str(input("Quem você está procurando? ")).strip()

try:
    # Conecta ao arquivo de banco de dados 'meubanco.db'.
    # O 'with' garante que a conexão será fechada automaticamente ao final.
    with sqlite3.connect("meubanco.db") as banco:
        cursor = banco.cursor()

        # Executa a busca no banco usando 'LIKE' e '?' para evitar ataques de SQL Injection.
        # O '%busca%' permite encontrar nomes que contenham o termo digitado em qualquer parte.
        cursor.execute("SELECT * FROM pessoas_detalhado WHERE nome LIKE ?", (f"%{busca}%",))

        total = 0 # Contador de registros encontrados
        hoje = date.today() # Pega a data atual do sistema

        # Percorre cada registro retornado pelo banco de dados
        # enumerate(..., start=1) conta os itens a partir de 1 e atualiza a variável 'total'
        for total, pessoa in enumerate(cursor , start=1):
            # print(f'{pessoa[1]} {pessoa[2]} nasceu em {pessoa[3]}')
            data_nasc = datetime.strptime(pessoa[3], "%Y-%m-%d").date()

            # Subtrai o ano atual pelo ano de nascimento e ajusta em -1 caso a pessoa ainda não tenha feito aniversário este ano
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
