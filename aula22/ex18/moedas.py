def dobro(preço, formato=False):
    dobro = preço*2
    if formato:
        return f"R${dobro:.2f}".replace('.', ',')
    else:
        return dobro

def metade(preço, formato=False):
    metade = preço/2
    return f"R${metade:.2f}".replace('.', ',') if formato else metade

def aumentar(preço, taxa, formato=False):
    aumentar = (preço*taxa) / 100 + preço
    return f"R${aumentar:.2f}".replace('.', ',') if formato else aumentar

def diminuir(preço, taxa, formato=False):
    diminuir = preço - ((preço*taxa) / 100 ) 
    return f"R${diminuir:.2f}".replace('.', ',') if formato else diminuir

def Formato(preço):
    return f"R${preço:.2f}".replace('.', ',')


def resumo(preço, taxa1=10, taxa2=5):
    print('--'*17)
    print('RESUMO DO VALOR'.center(30))
    print('--'*17)
    print(f'Preço analisado: \t{Formato(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa1}% de aumento: \t{aumentar(preço, taxa1, True)}')
    print(f'{taxa2}% de redução: \t{diminuir(preço, taxa2, True)}')
    print('--'*18)