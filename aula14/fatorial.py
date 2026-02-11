n = int(input('Digite um numero para calcular seu fatorial: '))

c = n 
f = 1

while c > 0:
    print(f'{c} x', end=' ')
    c -= 1
    f *= c
print(f'O fatorial de {n} é {f}')