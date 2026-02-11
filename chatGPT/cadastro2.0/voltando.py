def linha(tam = 20):
    return '--' * tam

def cabeçalho(msg):
    print(linha())
    print(msg.center(40))
    print(linha())

def ler_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Coloque um número real')
            continue
        else:
            return n
        
def ler_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Coloque um número inteiro!')
            continue
        else:
            return n

def LerNome(msg):
    while True:
        nome = str(input(msg)).strip()

        if nome == '':
            print('Digite o nome do produto para proseguir!')
            continue
        else:
            return nome
        
def cadastro():
    compras = dict()
    print(linha())
    compras['produto'] = LerNome('Nome do Produto: ')
    compras['preco'] = ler_float(f'Preço do {compras["produto"]}:  R$')
    return compras

def mostraProdutos(lista):
    for p in lista:
        print(f'{p['produto']:<20} R${p['preco']:>5}')

def menu(lista):
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    opc = ler_int('Digite sua opção: ')
    print(linha())
    return opc

def somar(lista):
    tot = sum(item['preco'] for item in lista)
    print(f'Ao todo sua compra deu R${tot:.2f} no total!')
    print(linha())

def mais_caro(lista):
    if not lista:
        print('Nenhum produto cadastrado!')
        return
    
    caro = lista[0]

    for item in lista:
        if item['preco'] > caro['preco']:
            caro = item
    print(f'Produto mais caro: {caro['produto']} R${caro['preco']:.2f}')
    print(linha())
    
def cadastrar_novamente(lista):
    while True:
        lista.append(cadastro())

        resp = ' '
        cabeçalho('CADASTRO REALIZADO1')
        while resp not in 'SN':
            resp = str(input('Quer continuar [S/N]: ')).strip().upper().split()[0]
        if resp not in 'SN':
            print('Por favor digite Sim ou Não')
        

        if resp == 'N':
            break

    


produtos = list()
nome = 'nome:'.upper()
preco = 'preço:'.upper()

while True:
    produtos.append(cadastro())

    resp = ' '
    cabeçalho('CADASTRO REALIZADO1')
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper().split()[0]
        if resp not in 'SN':
            print('Por favor digite Sim ou Não')
        

    if resp == 'N':
        break


cabeçalho('PRODUTOS')
print(f'{nome:<20} {preco:>5}')
mostraProdutos(produtos)
print(linha())

while True:
    opc = menu(['Somar', 'Item mais caro', 'Cadastrar novo produto', 'Sair do programa'])

    if opc == 1:
        somar(produtos)
    elif opc == 2:
        mais_caro(produtos)
    elif opc == 3:
        cadastrar_novamente(produtos)
        print(linha())
        print(f'{nome:<20} {preco:>5}')
        mostraProdutos(produtos)
        print(linha())
    elif opc == 4:
        break

        


        
