from operator import itemgetter
lista = {}
time = []
partidas = []

while True: 
    lista.clear()
    lista['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {lista['nome']} jogou? '))
    partidas.clear()
    for p in range(tot):
        partidas.append(int(input(f'Quantos gols na partida {p+1}? ')))

    lista['gols'] = partidas[:]
    lista['total'] = sum(partidas)
    time.append(lista.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper()[0]
        if continuar in 'SN':
            break
        else:
            print('ERRO! Digite S para sim e N para Não')
    
    if continuar == 'N':
        break
    print('-='*30)
    
print('-='*30)
for i in lista.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<13}', end='')
    print()
print('-='*30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com codigo {busca}')
    else:
        print(f'-- LEVANTEMENTO DO JOGADOR {time[busca] ['nome']} --')
        for i, g in enumerate(time[busca] ['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-='*30)