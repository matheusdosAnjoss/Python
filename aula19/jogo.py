from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador 1':randint(1,6),
    'jogador 2':randint(1,6),
    'jogador 3':randint(1,6),
    'jogador 4':randint(1,6)
}

ranking = ()

print('-='*20)
print('Valores sorteados')
print('-='*20)
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(0.8)
print('-='*20)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('== Ranking dos Jogadores ==')
print('-='*20)
for k, v in enumerate(ranking):
    print(f'{k+1} lugar {v[0]} tirou {v[1]}')
    sleep(0.5)

print('-='*20)