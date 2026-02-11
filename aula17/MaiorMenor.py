listaNum = []
maior = max(listaNum)
menor = min(listaNum)
for c in range(0,5):
    listaNum.append(int(input(f'Digite um valor para a posição {c}: ')))

print('-'*40)
print(f'Você digitou os valores {listaNum}')

print(f'O maior valor digitado foi {maior} nas posições {listaNum.index(maior)}...')

print(f'O menor valor digitado foi {menor} nas posições {listaNum.index(menor)}...')
print('-'*40)