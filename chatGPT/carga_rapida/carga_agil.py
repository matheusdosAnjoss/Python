
def linha(tam = 20):
    return '=='*tam

def titulo(msg):
    print(linha())
    print(msg.center(40))
    print(linha())

def ler_int(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('[red]ERRO! Digite um número inteiro!')
            continue
        else:
            return n
        
def ler_float(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('[red]ERRO! Digite um número real!')
            continue
        else:
            return n
        
def ler_nome(msg):
    while True:
        nome = str(input(msg))

        if nome == '':
            print('[red]ERRO: nenhum campo de texto pode ficar vazio!')
            continue
        else:
            return nome


def cadastro():
    pacote = dict()
    pacote['id'] = ler_nome("Digite o ID do pacote (ou 'FIM' para sair): ").upper()

    if pacote['id'] == 'FIM':
        return 'FIM'

    pacote['peso'] = ler_float('Digite o peso: Kg')

    while True:
        print('1 - Expressa\n2 - Normal\n3 - Economica')
        prioridade = ler_int('Prioridade: ')
        if prioridade in [1,2,3]:
            pacote['prioridade'] = prioridade
            break
        titulo('ERRO: digite 1, 2 ou 3!')

    return pacote
    
            #PROGRAMA PRINCIPAL
pacotes = []
limite_caminhao = 500.0

while True:
    titulo('Sistema de Carga')
    resultado = cadastro()

    if resultado == 'FIM':
        break

    pacotes.append(resultado)
    # 1. Ordenar por prioridade (1 é menor que 3, então vem primeiro)
    if len(pacotes) > 0:
        pacotes.sort(key=lambda p: p['prioridade'])

        caminhao = []
        peso_total = 0

        nomes_prioridade = {1: "Expressa", 2: "Normal", 3: "Economica"}

        for item in pacotes:
            if peso_total + item['peso'] <= limite_caminhao:
                caminhao.append(item)
                peso_total += item['peso']

        titulo('MANIFESTO DE EMBARQUE')
        print(f"{'ID':<10} | {'PESO':<8} | {'PRIORIDADE'}")
        print('-' * 40)

        for item in caminhao:
            item_nome = nomes_prioridade[item['prioridade']]
            print(f"{item[ 'id' ]:<10} | {item[ 'peso' ]:<6} Kg | {item_nome}")

        print(linha())
        print(f'Capacidade: {limite_caminhao}Kg')
        print(f'Carga Total: {peso_total}Kg ({(peso_total/limite_caminhao)*100:.1f}%)')
        print(f"Espaço Sobrando: {limite_caminhao - peso_total}Kg")
    else:
        print("Nenhum pacote cadastrado.")
    

print('FIM DO PROGRAMA!')
    