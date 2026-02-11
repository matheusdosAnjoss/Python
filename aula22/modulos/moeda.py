def dobro(preço, formato=False):
    dobro = preço*2
    if formato:
        return f"R${dobro:.2f}"
    else:
        return dobro

def metade(preço, formato=False):
    metade = preço/2
    return f"R${metade:.2f}" if formato else metade

def aumentar(preço, taxa, formato=False):
    aumentar = (preço*taxa) / 100 + preço
    return f"R${aumentar:.2f}" if formato else aumentar

def diminuir(preço, taxa, formato=False):
    diminuir = preço - ((preço*taxa) / 100 ) 
    return f"R${diminuir:.2f}" if formato else diminuir

def Format(preço):
    return f"{preço:.2f}"
