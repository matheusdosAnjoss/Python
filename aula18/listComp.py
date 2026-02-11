pessoas = []
dados = []
PesCadastrada = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Digite deu peso: Kg')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    pessoas.append(dados[:])
    PesCadastrada += 1
    dados.clear()

    if continuar == 'N':
        break

print('-='*30)
print(f'Ao todo você casdastrou {PesCadastrada} pessoas.')

maior = menor = pessoas[0][1]

for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    elif p[1] < menor:
        menor = p[1]
    
print(f'O maior peso foi {maior} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')


print(f'\nO menor peso foi {menor} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')

