n = cont = soma = 0

while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'Você digitou {cont} números')
print(f'A soma dos numeros são {soma}')