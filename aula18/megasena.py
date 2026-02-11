from random import randint
lista = []
jogos = []
quant = int(input('Quantos jogos você quer que eu sortei: '))
tot = 1

while tot <= quant:
    cont = 0 
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
    
print('-=' * 3,f'SORTEANDO {quant} JOGOS', '-=' * 4)

for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}')

print('-='*20)