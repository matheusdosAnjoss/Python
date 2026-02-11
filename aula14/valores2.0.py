res = 'S'
media = soma = quant = 0
numeros = []
while res in 'Ss':
    num = int(input('Digite um número: '))
    numeros.append(num)
    soma += num
    quant += 1
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

media = soma / quant
print(f'Você digitou {quant} números e a media foi {media:.2}')
print(f'O maior numero foi {max(numeros)} é o menor numero foi {min(numeros)}')
print('FIM')