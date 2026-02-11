from random import randint
lista =[randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)]

def SortValores():
    print(f'Sorteando 5 valores da lista: ', end='')
    for n in lista:
        print(f'{n}', end=' ')
    print('PRONTO!')

def SomaPares():
    soma = 0
    print(f'Somando valores pares de {lista},', end=' ')
    for n in lista:
        if n % 2 == 0:
            par = n
            soma += par
    print(f'temos {soma}')

def SomaImpares():
    soma = 0
    print(f'Somando os valores impares de {lista},', end=' ')
    for n in lista:
        if n % 2 == 1:
            impar = n
            soma += impar
    print(f'temos {soma}')

SortValores()
print('=='*25)
SomaPares()
print('=='*25)
SomaImpares()
