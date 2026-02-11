numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))

    res = ' '
    while res not in 'SN':
        res = str(input("Quer continuar? [S/N]: ")).upper().split()[0]

    if res == 'N':
        break

print('-='*30)
print(numeros)

for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista de pares é {pares}')
print(f'A Lista de impares é {impares}')