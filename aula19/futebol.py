from operator import itemgetter
lista = {}
partidas = []
cont = 0
lista['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {lista['nome']} jogou? '))

for p in range(tot):
    partidas.append(int(input(f'Quantos gols na partida {p+1}? ')))
 
print('-='*30)
lista['gols'] = partidas[:]
lista['total'] = sum(partidas)
print(lista)
print('-='*30)

for k, v in lista.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {lista['nome']} jogou {len(lista['gols'])} partidas')
for k, v in enumerate(lista['gols']):
    print(f'==> Na partida {k+1}, fez {v} gols')
print(f'Foi um total de {lista['total']} gols')