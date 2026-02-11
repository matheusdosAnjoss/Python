def linha(tam = 20):
    return '--'*tam

def titulo(msg):
    print(linha())
    print(msg.center(40))
    print(linha())

def ler_nome(msg):
    while True:
        nome = str(input(msg))

        if nome == '':
            print('Por favor digite um nome valido!')
            continue
        else:
            return nome

def ler_int(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print('Por favor coloque um numero valido')
            continue
        else:
            return n
        
def menu():
    titulo('SISTEMA DE CONTROLE LOGISTICO')
    opcao = ['Cadastrar nova entrega', 'Listar todas as entregas', 'Atualizar status da entrega', 'Buscar entregar por codigo', 'Relatorio de entregas', 'Sair do sistema']

    c = 1
    for v in opcao:
        print(f'{c} - {v}')
        c += 1

    opc = ler_int('Escolha uma opção: ') 
    return opc

def cadastro_de_entrega():
    cadastro = dict()
    
    cadastro['codigo'] = ler_int('Código da entrega: ')
    cadastro['nome'] = ler_nome('Nome do Cliente: ')
    cadastro['cidade'] = ler_nome('Cidade de destino: ')
    cadastro['peso'] = ler_int('Peso da carga: Kg')
    cadastro['veiculo'] = ler_nome('Veiculo: ')
    cadastro['nome motorista'] = ler_nome('Motorista: ')
    cadastro['status'] = ler_nome('Status inicial: ').lower()
    return cadastro
    
def lista_de_entregas(lista):
    if not lista:
        titulo('Nenhuma Lista cadastrada!')
        return

    for item in lista:
        print(f'Código: {item['codigo']}')
        print(f'Cliente: {item['nome']}')
        print(f'Destino: {item['cidade']}')
        print(f'Peso: {item['peso']}')
        print(f'Veiculo: {item['veiculo']}')
        print(f'Motorista: {item['nome motorista']}')
        print(f'Status: {item['status']}')
        print(linha())

def att_status(lista):
    if not lista:
        titulo('Nenhuma lista cadastrada!')
        return
    
    print(linha())
    codigo = ler_int('Informe o código da entrega: ')

    for entrega in lista:
        if entrega['codigo'] == codigo:

            if entrega['status'] == "entregue":
                titulo(f'Erro: esta entrega já foi finalizada e não pode ser alterada')
                return
            
            print(f'Status atual: {entrega['status']}')
            print('Escolha o novo status: ')
            print('1 - Pedente')
            print('2 - Em tranporte')
            print('3 - Entregue')

            opcao = ler_int('Opção: ')

            if opcao == 1:
                entrega['status'] = 'Pendente'
            elif opcao == 2:
                entrega['status'] = 'Em Transporte'
            elif opcao == 3:
                entrega['status'] = 'entregue'
            else:
                print('Opção invalida.')
                return
            
            print(f'Status atualizado com sucesso! para {entrega['status']}')
            return
        
    print('ERRO entrega não encontrada')
    
def buscar_entrega(lista):
    if not lista:
        titulo(f'Nenhuma lista cadastrada!')
        return
    
    print(linha())
    codigo = ler_int('Informe o codigo da entregar: ')

    for item in lista:
        if item['codigo'] == codigo:
            titulo('Dados da entrega')
            print(f'Cliente: {item['nome']}')
            print(f'Destino: {item['cidade']}')
            print(f'Peso: {item['peso']}')
            print(f'Veiculo: {item['veiculo']}')
            print(f'Motorista: {item['nome motorista']}')
            print(f'Status: {item['status']}')

def relatorio_da_entrega(lista):
    if not lista:
        titulo(f'Nenhuma lista cadastrada!')
        return

    tot_entregas = len(lista)
    pendentes = 0
    transporte = 0
    entregues = 0
    peso_tot = 0
    peso_entregue = 0

    for item in lista:
        peso_tot += item['peso']

        if item['status'] == 'pendente':
            pendentes += 1
        elif item['status'] == 'em transporte':
            transporte += 1
        elif item['status'] == 'entregue':
            entregues += 1
            peso_entregue += item['peso']

    titulo('RELATÓRIO LOGÍSTICO')
    print(f'Total de entregas: {tot_entregas}')
    print(f'Pendentes: {pendentes}')
    print(f'Em tranporte: {transporte}')
    print(f'Entregues: {entregues}')
    print(f'Peso total transportado: {peso_tot} Kg')
    print(f'Peso total entregue: {peso_entregue} Kg')


            # PROGRAMA PRINCIPAL

cadastros = []

while True:
    opcao = menu()

    if opcao == 1:
        titulo('CADASTRO DE ENTREGA')
        cadastros.append(cadastro_de_entrega())
        titulo('Entrega cadastrada com sucesso!')
    elif opcao == 2:
        titulo('LISTA DE ENTREGAS')
        lista_de_entregas(cadastros)
    elif opcao == 3:
        att_status(cadastros)
    elif opcao == 4:
        buscar_entrega(cadastros)
    elif opcao == 5:
        relatorio_da_entrega(cadastros)
    elif opcao == 6:
        break
titulo('Obrigado por usar o Sistema de Controle Logístico.')
