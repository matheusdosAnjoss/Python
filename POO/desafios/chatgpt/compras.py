def ler_nome(msg):
    while True:
        n = str(input(msg))
        
        if n == '':
            print('ERRO: tente novamente!')
            continue
        else :
            return n

def ler_int(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('[red]ERRO! Digite um número inteiro!')
            continue
        else:
            return n

class mercado:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class listaDeCompras:
    def __init__(self):
        self.lista = []

    def adicionarCompras(self, compras):
        self.lista.append(compras)

    def listaProdutos(self):
        if not self.lista:
            print('Nenhum Produto cadastrado!')
        
        for item in self.lista:
            print(f'Produto: {item.nome}')
            print(f'Preço: {item.preco:.2f}')
            print('='*20)

    def totalCompras(self):
        total = 0

        for item in self.lista:
            total += item.preco
        return total

class continuar:
    def pergurtar(self):
        while True:
            resp = input("Deseja continuar? [S/N] ").strip().lower()

            if resp == 's':
                return True
            elif resp == 'n':
                return False
            else:
                print("Opção inválida! Digite apenas S ou N.")



#        Programa Principal
compras = listaDeCompras()
controle = continuar()

while True:
    print("\n===== BIBLIOTECA =====")
    print("1 - Adicionar produto")
    print("2 - Listar das compras")
    print("3 - Sair")

    opcao = ler_int('Qual sua opção: ')

    if opcao == 1:
        nome = input('Nome do produto: ')
        preco = float(input('Preço do produto: R$'))
    
        produtos = mercado(nome, preco)
        compras.adicionarCompras(produtos)

        if not controle.pergurtar():
            break

    elif opcao == 2:
        print('='*20)
        compras.listaProdutos()
    elif opcao == 3:
        break

print('='*20)
print(f"Total de compras foi de R${compras.totalCompras():.2f}")