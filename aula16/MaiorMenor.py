from random import randint
sorteador = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10),)
Maior = max(sorteador)
Menor = min(sorteador)

print('Os valores sorteados foram:', end=' ')
for c in sorteador:
    print(f'{c}', end=' ')

print(f'\nO maior valor sorteado foi {Maior}')
print(f'O menor valor sorteado foi {Menor}')
