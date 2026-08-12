
class Porta:
    def abrir(self):
        print('Girar a maçaneta e empurrar/puxar a porta')


class Ovo:
    def abrir(self):
        print('Quebre a casca com um garfo e separe as partes sobre uma frigideira')

class Pedra:
    pass
        


def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f'Encontrei problemas ao tentar abrir {objeto.__class__.__name__}')


a = Porta()
b = Ovo()
c = Pedra()

tentar_abrir(a)
tentar_abrir(b)
tentar_abrir(c)