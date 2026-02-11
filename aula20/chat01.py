from random import randint
lista =[randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)]
soma = 0

#def Multiplicar():



for c in lista:
    if c % 2 == 0:
        par = c
        soma = soma * par
print(f'Sorteando 5 Numeros aleatorios: {lista}')
print(soma)
#Multiplicar()