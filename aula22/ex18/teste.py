import moedas 

num = float(input('Digite o preço: R$'))

#print('=='*18)
#print(f'A metade de {moedas.Formato(num)} é {moedas.metade(num, True)}')
#print(f'O dobro de {moedas.Formato(num)} é {moedas.dobro(num, True)}')
#print(f'Aumentando 10%, temos {moedas.aumentar(num, 10, True)}')
#print(f'Diminuindo 13%, temos {moedas.diminuir(num, 13, True)}')
#print('=='*18)

moedas.resumo(num, 20, 12)