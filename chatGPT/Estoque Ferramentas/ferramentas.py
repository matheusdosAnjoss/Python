def linha(tam = 20):
    return '--' * tam

def titulo(msg):
    print(linha())
    print(msg.center(40))
    print(linha())

def ler_int(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print('Por favor digite um numero inteiro!')
            continue
        else:
            return n
        
def ler_float(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('Por Favor digite um número real!')
            continue
        else:
            return n
        
def ler_nome(msg):
    while True:
        nome = str(input(msg)).strip()

        if nome == '':
            print('Por Favor digite o nome da ferramenta!')
            continue
        else:
            return nome
        
def menu():
    opcao = ['Cadastrar nova ferramenta', 'Entrada de ferramentas', 'Saida de ferramentas', 'Devolução de ferramentas', 'Listar ferramentas', 'Relatorio geral', 'Sair']
    c = 1
    for v in opcao:
        print(f'{c} - {v}')
        c += 1

    print(linha())
    res = ler_int('Sua opção: ')
    return res

def cadastrar_ferramentas():
    print(linha())
    nome = ler_nome('Nome da Ferramenta: ').lower()

    for item in ferramentas:
        if item['nome'].lower() == nome:
            titulo('ERRO: Já existe ferramenta com esse nome!')
            return
        
    quantidade = ler_int('Quantidade Inicial: ')

    nova_ferramenta = {'nome': nome.title(),
                   'quantidade': quantidade,
                    'emprestado': 0}
    return nova_ferramenta
    

def desejar_continuar(msg= 'Quer continuar?[S/N] '):
    res = ' '
    while res not in 'SN':
        res = str(input(msg)).upper().split()[0]
        if res not in 'SN':
            print('Digite S para sim e N para não!')
    return res

def lista_ferramentas(lista):
    if not lista:
        titulo('Nenhuma farramenta cadastrada!')
        return
    
    for v in lista:
        print(f'Nome: {v['nome']:<15} Quantidade: {v['quantidade']:>2}')


def entrada_de_ferramentas(lista):
    if not ferramentas:
        titulo('Nenhuma ferramenta cadastrada!')
        return
    
    titulo('Ferramentas Disponiveis:')
    
    for i, item in enumerate(lista):
        print(f'{i+1} - {item['nome']} (Qtd: {item['quantidade']})')

    while True:
        esc = ler_int('Escolha a ferramenta: ') - 1

        if 0 <= esc < len(ferramentas):
            break
        else:
            print('Número ivalido!')
            
    while True:
        qtd = ler_int('Quantidade para adicionar: ')
        if qtd >= 0:
            break
        print('A quantidade não pode ser negativa!')

    ferramentas[esc]['quantidade'] += qtd

    titulo(f'Entrada registrada! Estoque atualizado de {ferramentas[esc]['nome']}')


def saida_ferramentas(lista):
    if not ferramentas:
        print('Nenhuma ferramenta cadastrada!')
        return
    
    titulo('SAIDA DE FERRAMENTAS')

     #LISTA DE FERRAMENTAS
    for i, item in enumerate(lista):
        print(f'{i+1} - {item['nome']} (Qtd: {item['quantidade']})')

    #ESCOLHER FERRAMENTA
    while True:
        esc = ler_int('Excolhar a ferramenta: ') -1

        if 0 <= esc < len(lista):
            break
        else:
            print('Número ínvalido')

    #INFORMA A QUANTIDADE
    while True:
        qtd = ler_int('Quantidade para retirar: ')

        if 0 <= qtd <= lista[esc]['quantidade']:
            break
        print('Quantidade indisponivel!')

    #ATUALIZAR ESTOQUE
    lista[esc]['quantidade'] -= qtd
    lista[esc]['emprestado'] += qtd
    print(f'Saida registrada! Eastoque atualizado de {lista[esc]['nome']} ')

def devolucao_ferramentas(lista):
    if not lista:
        titulo('Nenhuma ferramenta cadastrada!')
        return
    
    titulo('DEVOLUÇÂO DE FERRAMENTAS')

    #MOSTRA APENAS FERRAMENTAS EMPRESTADAS
    emprestadas = []
    for item in lista:
        if item['emprestado'] > 0:
            emprestadas.append(item)

    if not emprestadas:
        print('Nenhuma ferramenta emprestada no momento.')
        return
    
    for i, item in enumerate(emprestadas):
        print(f'{i+1} - {item['nome']} (Emprestadas: {item['emprestado']})')

    print(linha())

    #ESCOLHER FERRAMENTA
    while True:
        esc = ler_int('Escolhar a ferramenta: ') -1
        if 0 <= esc < len(emprestadas):
            break
        else:
            print('Opção invalida!')

    ferramenta = emprestadas[esc]

    #QUANTIDADE DEVOLVIDA
    while True:
        qtd = ler_int('Quantidade devolvida: ')
        if 0 <= qtd <= ferramenta['emprestado']:
            break
        else:
            print("Quantidade invalida!")

    #ATUALIZAR ESTOQUE
    ferramenta['quantidade'] += qtd
    ferramenta['emprestado'] -= qtd

    print(f'Devolução resgistrada! {ferramenta['nome']} Qtd: {ferramenta['quantidade']} (atualizada)')


def relatorio_geral(lista):
    if not lista:
        titulo("Nenhuma ferramenta cadastrada!")
        return
    
    total_ferramentas = len(lista)
    total_disponivel = 0
    total_emprestado = 0

    mais_emprestada = None
    menor_disponivel = None

    for item in lista:
        total_disponivel += item['quantidade']
        total_emprestado += item['emprestado']

        if mais_emprestada is None or item['emprestado'] > mais_emprestada['emprestado']:
            mais_emprestada = item

        if menor_disponivel is None or item['quantidade'] < menor_disponivel['quantidade']: 
            menor_disponivel = item

    print(f'Total de ferramentas cadastradas: {total_ferramentas}')
    print(f'Total disponível no estoque: {total_disponivel}')
    print(f'Total emprestado: {total_emprestado}')

    if mais_emprestada['emprestado'] > 0:
        print(f'Ferramentas mais emprestada: {mais_emprestada['nome']} ({mais_emprestada['emprestado']})')
    else:
        print('Nenhuma ferramenta emprestada')

    print(f'Ferramentas com menor disponibilidade: {menor_disponivel['nome']} ({menor_disponivel['quantidade']})')




                    #PROGRAMA PRINCINPAL
ferramentas = []

while True:
    titulo('CONTROLE DE FERRAMENTAS')
    opcao = menu()

    if opcao == 1:
        while True:
            novo = cadastrar_ferramentas()
            if novo: # != None
                ferramentas.append(novo)
                titulo('Ferramenta cadastrada')

            if desejar_continuar() == 'N':
                break
    elif opcao == 2:
        entrada_de_ferramentas(ferramentas)
    elif opcao == 3:
        saida_ferramentas(ferramentas)
    elif opcao == 4:
        devolucao_ferramentas(ferramentas)
    elif opcao == 5:
        titulo('ESTOQUE')
        lista_ferramentas(ferramentas)
    elif opcao == 6:
        titulo('RELATÓRIO GERAL')
        relatorio_geral(ferramentas)
    elif opcao == 7:
        break