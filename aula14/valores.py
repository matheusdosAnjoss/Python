numero = 0
cont = 0
soma = 0

numero = int(input('Digite um número [999 para PARAR]: '))

while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número [999 para PARAR]: '))


print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
print('FIM')