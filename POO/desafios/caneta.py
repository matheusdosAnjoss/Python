from rich import print

class Caneta:
    def __init__(self, cor = 'azul'):
        escolha = ""
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case _:
                escolha = 'white'
            
        self.cor = escolha
        self.tampada = True

    def escrever(self, msg):
        if self.tampada:
            print(f'A {self.cor}caneta[/] esta tampada!')
        else:
            print(f'{self.cor}{msg}', end=' ')

    def quebraLinha(self, qtd= 1 ):
        print('\n' * qtd, end='')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False



c1 = Caneta(cor='vermelho')
c1.destampar()
c1.escrever('Olá mundo!')
c1.quebraLinha(2)

c2 = Caneta(cor='verde')
c2.escrever('Olá mundo!')
c2.quebraLinha(2)

c3 = Caneta(cor='azul')
c3.destampar()
c3.escrever('Olá mundo!')



