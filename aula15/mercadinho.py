somaPreco = 0
MaisDeMil = 0
MaisBarato = 0
NomeMaisBarato = '' 
primeiro = True
while True:
    print('--'*25)
    print('LOJA SUPER BARATÃO')
    print('--'*25)

    produto = str(input('Nome do Produto: '))

    preco = float(input('Preço: R$'))
    somaPreco += preco
    if preco >= 1000:
        MaisDeMil += 1

    if primeiro or preco < MaisBarato:
        MaisBarato = preco
        NomeMaisBarato = produto
        primeiro = False
    

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).upper().split()[0]
        if continuar in ['S', 'N']:
            break
        else:
            print('Digite S para SIM e N para NÂO...')
    if continuar == 'N':
        break
print('--'*25)
print(f'O total da compra foi de R${somaPreco:.2f}')
print(f'Temos {MaisDeMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {NomeMaisBarato} que custa R${MaisBarato:.2f}')
print('--'*25)
print('FIM')