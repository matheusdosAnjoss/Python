numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    n = int(input('Diigite um numero entre 0 e 10: '))

    if 0 <= n <= 10:
        print(f'Você digitou o número {numeros[n]}')
        break
    print('Tente Novamente. Digite um número entre 0 e 10')