from modulos import moeda

num = float(input('Digite o preço: R$'))
print('=='*15)
print(f'A metade de {moeda.Format(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {num:.2f} é {moeda.dobro(num, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(num, 13, True)}')