def linha(tam = 20):
    return '--'*tam

def titulo(msg):
    print(linha())
    print(msg.center(40))
    print(linha())

def ler_int(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO! Digite um número inteiro!')
            continue
        else:
            return n
        
def ler_float(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO! Digite um número real!')
            continue
        else:
            return n
        
def ler_nome(msg):
    while True:
        nome = str(input(msg))

        if nome == '':
            print('Por favor digite o nome do adubo')
            continue
        else:
            return nome

def menu():
    print(linha())
    opcao = ['Cadastrar Adubos', 'Entrada De Adubos', 'Saída de Adubos', 'Lista de Adubos', 'Relatorio Geral' ,'Sair']
    c = 1
    for i in opcao:
        print(f'{c} - {i}')
        c += 1
    print(linha())
    opc = ler_int('Qual a sua Opção: ')
    return opc

def cadastrar_abubo():
    print(linha())
    nome = ler_nome('Nome ou Codigo do adubo: ')

    for item in adubos:
        if item['nome'].lower() == nome:
            titulo('ERRO ja existe esse nome!')
            return
        
    quantidade = ler_int('Quantidade inicial: ')

    novo_adubos = {'nome': nome.title(),
                    'quantidade': quantidade}
    return novo_adubos
    
def continuar(msg='Desejar continuar? '):
    res = ' '
    while res not in 'SN':
        res = str(input(msg)).upper()
        if res not in 'SN':
            print('ERRO! Digite S para SIM e N para NÃO')
            continue
        return res

def lista_adubos(lista):
    if not lista:
        titulo('Nenhuma lista cadastrada!')
        return
    
    for i, item in enumerate(lista):
        print(f'{i+1} - {item['nome']} - Qtd: {item['quantidade']}')


def entrada_de_adubos(lista):
    if not lista:
        titulo('Nenhum adubo cadastrado!')
        return
    
    for i, item in enumerate(lista):
        print(f'{i+1} - {item['nome']} (Qtd: {item['quantidade']})')

    while True:
        escolha = ler_int('Escolhar o adubo: ') -1

        if 0 <= escolha < len(lista):
            break
        else:
            print('Numero invalido')

    while True:
        qtd = ler_int('Quantidade para adicionar: ')

        if qtd > 0:
            break
        else:
            print("O número não pode ser negativo!")

    lista[escolha]['quantidade'] += qtd 

    titulo(f'Entrada registrada! Estoque atualizado de {lista[escolha]['nome']} (Qtd: {lista[escolha]['quantidade']})')


def saida_de_adubos(lista):
    if not lista:
        print('Nenhum abubo cadastrado!')
        return
    
    for i, item in enumerate(lista):
        print(f'{i+1} - {item['nome']} - (Qtd: {item['quantidade']})')

    while True:
        escolha = ler_int('Escolha o adubo: ') -1
        if 0 <= escolha < len(lista):
            break
        else:
            print('Número Invalido')

    while True:
        qtd = ler_int('Quantidade para retirar: ')
    
        if 0 <= qtd <= lista[escolha]['quantidade']:
            break
        else:
            print('Numero invalido!')

    lista[escolha]['quantidade'] -= qtd
    titulo(f'Entrada registrada! Estoque atualizado de {lista[escolha]['nome']} (Qtd: {lista[escolha]['quantidade']})')


def relatorio_geral(lista):
    if not lista:
        print('Nenhum produto cadastrado!')
        return
    
    total_adubos = len(lista)
    total_estoque = 0
    maior_qtd = lista[0]
    menor_qtd = lista[0]

    for item in lista:
        total_estoque += item['quantidade']

        if item['quantidade'] > maior_qtd['quantidade']:
            maior_qtd = item
        elif item['quantidade'] < menor_qtd['quantidade']:
            menor_qtd = item

    print(linha())
    print(f'Total de adubos cadastrado: {total_adubos}')
    print(f'Total Disponivel no estoque: {total_estoque}')

    print(f'O adubo com MAIOR quantidade é: {maior_qtd['nome']} (Qtd: {maior_qtd['quantidade']})')

    print(f'O adubo com MENOR quantidade é: {menor_qtd['nome']} (Qtd: {menor_qtd['quantidade']})')

#                     PROGRAMA PRINCIPAL

adubos = []

while True:
    opcao = menu()

    if opcao == 1:
        while True:
            novo = cadastrar_abubo()
            if novo:
                adubos.append(novo)
                titulo('Adubo Cadastrado!')
            
            if continuar() == 'N':
                break
    
    elif opcao == 2:
        titulo('Lista de Adubos')
        entrada_de_adubos(adubos)

    elif opcao == 3:
        titulo('Lista dos Adubos')
        saida_de_adubos(adubos)
    
    elif opcao == 4:
        titulo('Lista dos Adubos')
        lista_adubos(adubos)

    elif opcao == 5:
        relatorio_geral(adubos)

    elif opcao == 6:
        titulo('FIM DO PROGRAMA')
        break
    