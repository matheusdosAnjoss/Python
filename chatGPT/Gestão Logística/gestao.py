from rich import print
from rich.panel import Panel
from rich.traceback import install
install()


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

def menu():
    titulo('SISTEMA DE GESTÃO LOGÍSTICA')
    opcao = ['Cadastrar encomenda', 'Listar encomendas', 'Atualizar status da encomenda', 'Cadastrar veiculo', 'Alocar encomenda em veiculo', 'Relatório logístico', 'Buscar encomenda', 'Sair']
    c = 1
    for v in opcao:
        print(f'{c} - {v}')
        c += 1
    
    opc = ler_int('Escolha uma opção: ')
    return opc

def gerar_codigo():
    return f"ENC{len(lista_encomenda) + 1:03d}"

def cadastrar_encomenda():
    cadastro = dict()
    print(linha())
    cadastro['nome'] = ler_nome('Nome do Cliente: ').upper()
    cadastro['cidade origem'] = ler_nome('Cidade de origem: ')
    cadastro['cidade destino'] = ler_nome('Cidade de Destino: ')
    cadastro['peso'] = ler_float('Peso da encomenda: Kg')
    cadastro['frete'] = ler_int('Valor do frete: R$')

    cadastro['codigo'] = gerar_codigo()
    cadastro['status'] = 'Pendente' 
    
    titulo('[green]Encomenda cadastrada com sucesso')
    print(f'[green]Codigo: {cadastro['codigo']}')
    print(f'[green]Status: {cadastro['status']}')
    return cadastro

def lista_encomendas(lista):
    if not lista:
        titulo('[red]Nenhuma Lista de encomenda encontrada!')
        return
    
    titulo('LISTA DE ENCOMENDAS')

    for item in lista:
        print(linha())
        print(f'Codigo: {item['codigo']}')
        print(f'Cliente {item['nome']}')
        print(f'Origem: {item['cidade origem']}')
        print(f'Destino: {item['cidade destino']}')
        print(f'Peso: {item['peso']}')
        print(f'frete: {item['frete']}')
        print(f'Status: {item['status']}')


def cadastrar_veiculo():
    cadastroV = dict()
    print(linha())
    cadastroV['placa'] = ler_nome('Placa do veiculo: ').upper()
    cadastroV['veiculo'] = ler_nome('Tipo do veiculo: ')
    cadastroV['capacidade'] = ler_float('Capacidade maxima (kg): ')
    cadastroV['status'] = 'Disponivel'
    cadastroV['encomenda'] = None
    print('[green]Veiculo cadastrado com sucesso!')
    print(f'Status: {cadastroV['status']}')
    return cadastroV


def alocar_encomenda(lista_encomendas, lista_veiculos):
    if not lista_encomendas:
        titulo("[red]ERRO: nenhuma encomenda cadastrada!")
        return
    
    print(linha())

    codigo = ler_nome('Informe o código da encomenda: ').strip().upper()
    placa = ler_nome('Informe a placa do veiculo: ').strip().upper()

    encomenda_encontrada = None
    veiculo_encontrado = None

    #PROCURAR ENCOMENDA
    for item in lista_encomendas:
        if item['codigo'] == codigo:
            encomenda_encontrada = item
            break
    
    if encomenda_encontrada is None:
        print('[red]ERRO: encomenda não encontrada')
        return
    
    if encomenda_encontrada['status'] != 'Pendente':
        print('[red]Erro: encomenda não está pendente.')
        return
                
    # PROCURAR VEICULO
    for item in lista_veiculos:
        if item['placa'] == placa:
            veiculo_encontrado = item
            break
    
    if veiculo_encontrado is None:
        print('[red]ERRO: veiculo não encontrado.')
        return
    
    if veiculo_encontrado['status'] != 'Disponivel':
        print('[red]ERRO: veiculo não esta disponivel')
        return
    
    if encomenda_encontrada['peso'] > veiculo_encontrado['capacidade']:
        titulo('[red]ERRO: peso da encomenda excede a capacidade do veiculo.')
        return
    
    #ALOCAÇÂO
    encomenda_encontrada['status'] = 'Em rota'
    veiculo_encontrado['status'] = 'Em uso'
    veiculo_encontrado['encomenda'] = encomenda_encontrada['codigo']

    titulo('[green]Encomenda alocada com sucesso!')
    print(f'[green]Encomenda {codigo}  -> Veiculo {placa}')


def atualizar_status(lista):
    if not lista:
        titulo('[red]ERRO: Cadastre um produto!')
        return
    print(linha())

    codigo = ler_nome('Informe o código da encomenda: ').upper()

    for entrega in lista:
        if entrega['codigo'] == codigo:
            if entrega['status'] == 'Entregue':
                titulo(f'[red]Erro: esta entrega já foi finalizada e não pode ser alterada')
                return
        else:
            titulo('[red]ERRO: Codigo não encontrado!')
            break

        caixa = Panel('1 - Em rota\n2 - Entregue', title='Novo Status', width=25, style='green')
        print(caixa)

        opcao = ler_int('Escolha: ')

        if opcao == 1:
            entrega['status'] = 'Em rota'
        elif opcao == 2:
            entrega['status'] = 'Entregue'
        else:
            print('Opção invalida!')
            return
            
        print('[green]Status atualizado com sucesso!')
        if entrega['status'] == 'Entregue':
            print(f'Encomenda {entrega['codigo']} marcada como ENTREGUE.')
            return


def buscar_encomenda(lista):
    if not lista:
        titulo('[red]ERRO: cadastre um produto!')
        return

    caixa = Panel('1 - Codigo\n2 - Nome do cliente', title='Buscar por:', width=25, style='green')
    print(caixa)

    opcao = ler_int('Escolha: ')

    if opcao == 1:
        cod = ler_nome('Digite o codigo: ').upper()
        for item in lista:
            if item['codigo'] == cod:
                titulo('[green]DADOS DA ENTREGAR')
                print(f'Codigo: {item['codigo']}')
                print(f'Cliente {item['nome']}')
                print(f'Origem: {item['cidade origem']}')
                print(f'Destino: {item['cidade destino']}')
                print(f'Peso: {item['peso']}')
                print(f'frete: {item['frete']}')
                print(f'Status: {item['status']}')
    elif opcao == 2:
        nome = ler_nome('Nome do cliente: ').upper()
        for item in lista:
            if item['nome'] == nome:
                titulo('[green]DADOS DA ENTREGAR')
                print(f'Codigo: {item['codigo']}')
                print(f'Cliente {item['nome']}')
                print(f'Origem: {item['cidade origem']}')
                print(f'Destino: {item['cidade destino']}')
                print(f'Peso: {item['peso']}')
                print(f'frete: {item['frete']}')
                print(f'Status: {item['status']}')
    else:
        titulo('[red]Opção Invalida Tente Novamente!')
        return


def relatorio(lista, lista_veiculos):
    if not lista:
        titulo('[red]ERRO: cadastre um produto!')
        return
    
    totalEcomendas = len(lista)
    pedentes = 0
    EmRota = 0
    entregue = 0
    faturamentoTotal = 0

    for item in lista:
        faturamentoTotal += item['frete']

        if item['status'] == 'Pendente':
            pedentes += 1
        elif item['status'] == 'Em rota':
            EmRota += 1
        elif item['status'] == 'Entregue':
            entregue += 1
        
    titulo('RELATORI LOGISTICO')
    print(f'Total de encomendas: {totalEcomendas}')
    print(f'Pendentes: {pedentes}')
    print(f'Em rota: {EmRota}')
    print(f'Entregues: {entregue}')
    print()
    print(f'Faturamento total: R${faturamentoTotal:.2f}')

    veiculo = len(lista_veiculos)
    veiculo = 0
    disponivel = 0
    Emuso = 0

    for item in lista_veiculos:
        if item['status'] == 'Disponivel':
            disponivel += 1
        elif item['status'] == 'Em uso':
            Emuso += 1

    print()
    print(f'Veiculos cadastrado: {veiculo}')
    print(f'Disponivel: {disponivel}')
    print(f'Em uso: {Emuso}')


                 #PROGRAMA PRINCINPAL
lista_encomenda = []
lista_veiculos = []

while True:
    opcao = menu()

    if opcao == 1:
        lista_encomenda.append(cadastrar_encomenda())
    elif opcao == 2:
        lista_encomendas(lista_encomenda)
    elif opcao == 3:
        atualizar_status(lista_encomenda)
    elif opcao == 4: 
        lista_veiculos.append(cadastrar_veiculo())
    elif opcao == 5:
        alocar_encomenda(lista_encomenda, lista_veiculos)
    elif opcao == 6:
        relatorio(lista_encomenda, lista_veiculos)
    elif opcao == 7:
        buscar_encomenda(lista_encomenda)
    elif opcao == 8:
        print(linha())
        print('[green]Sistema encerrado.')
        print('[green]Obrigado por utilizar o sistema de gestão Logistica!')
        print(linha())
        break
