def linha(tam = 20):
    return '--' * 20

def ler_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('Por favor coloque um número inteiro!')
            continue
        else:
            return n
        
def ler_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('Por favor coloque um número real!')
            continue
        else:
            return n
        
def ler_nome(msg):
    while True:
        nome = str(input(msg)).strip()
        if nome == '':
            print('Por favor digite o nome do produto')
            continue
        else:
            return nome

def cabeçalho(msg):
    print(linha())
    print(msg.center(40))
    print(linha())

def menu():
    ordem = ('Cadastrar produto', 'Entrada de estoque', 'Saida de estoque', 'Mostra estoque', 'Relatório de preço', 'Ranking dos Preços' ,'Sair')
    c = 1
    for v in ordem:
        print(f'{c} - {v}')
        c += 1

    print(linha())
    opc = ler_int('Qual a sua opção: ')
    return opc

def cadastrar_produtos():
    cadastro = dict()
    print(linha())
    cadastro['nome'] = ler_nome('Nome do produto: ')
    cadastro['quantidade'] = ler_int('Quantidade inicial: ')
    cadastro['preço'] = ler_float('Preço: ')
    return cadastro

def desejar_continuar(msg="Cadastrar outro? [S/N] "):
    while True:
        res = ' '
        while res not in 'SN':
            res = str(input(msg)).upper().split()[0]
            if res not in 'SN':
                print('Digite S para Sim e N para Não!')
        return res
    
def mostrar_estoque(lista):
    if not lista:
        print('Estoque vazio')
        return
    
    for v in lista:
        print(f"Produto: {v['nome']} | Qtde: {v['quantidade']} | preço: R${v['preço']:.2f}")

def entrada_estoque(lista):
    if not lista:
        cabeçalho('Estoque vazio! cadastre um produto!')
        return

    nome = ler_nome('Nome do produto: ').strip()

    for p in lista:
        if p['nome'].lower() == nome.lower():
            while True:
                qtd = ler_int('Quantidade para adicionar: ')
                if qtd <= 0:
                    print('Digite uma quantidade maior que zero')
                    continue
                
                p['quantidade'] += qtd
                cabeçalho(f'Estoque atualizado! agora {p['nome']} tem {p['quantidade']} unidades')
                return
                
    cabeçalho('Produto não encotrado!')
    
def saida_de_estoque(lista):
    nome = ler_nome('Nome do produto: ')

    for p in lista:
        if p['nome'].lower() == nome.lower():
            while True:
                qtd = ler_int('Quantidade para retirar: ')

                if qtd <= 0:
                    print('Digite uma quantidade maior que zero!')
                elif qtd > p['quantidade']:
                    print(f'Estoque insuficiente! Disponível: {p['quantidade']} unidades')
                else:
                    p['quantidade'] -= qtd
                    cabeçalho(f'Estoque atualizado agora {p['nome']} tem {p['quantidade']} unidades')
                    return
            
def mais_caro(lista):
    if not lista:
        cabeçalho('Nenhum produto cadastrado!')
        return

    caro = lista[0]

    for item in lista:
        if item['preço'] > caro['preço']:
            caro = item

    print(f"Produto mais caro: {caro['nome']} R${caro['preço']:.2f}")


def mais_barato(lista):
    barato = lista[0]

    for item in lista:
        if item['preço'] < barato['preço']:
            barato = item

    print(f'Produto mais barato: {barato['nome']} R${barato['preço']:.2f}')

def ranking_preço(lista):
    if not lista:
        cabeçalho('Nenhum produto cadastrado!')
        return
    
    rank = sorted(lista, key=lambda item: item['preço'], reverse=True)

    cabeçalho('RANKING DE PREÇO')

    for pos, p in enumerate(rank, start=1):
        print(f"{pos}º - {p['nome']} R${p['preço']:.2f}")






# PROGRAMA PRINCIPAL
produtos = []

while True:
    cabeçalho('SISTEMA DE ESTOQUE')
    opcao = menu()

    if opcao == 1:
        while True:
            produtos.append(cadastrar_produtos())

            cabeçalho('Cadastro realizado')
            if desejar_continuar() == 'N':
                break

    elif opcao == 2:
        entrada_estoque(produtos)
    elif opcao == 3:
        saida_de_estoque(produtos)
    elif opcao == 4:
        cabeçalho('ESTOQUE ATUAL')
        mostrar_estoque(produtos)
    elif opcao == 5:
        print(linha())
        mais_caro(produtos)
        mais_barato(produtos)
    elif opcao == 6:
        ranking_preço(produtos)
    elif opcao == 7:
        break


    