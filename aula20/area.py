def area(larg, comp):
    s = larg*comp
    print(f'A área de um terreno {larg} X {comp} é de {s}m²')

print('CONTROLE DE TERRENOS')
print('---'*10)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura,comprimento)