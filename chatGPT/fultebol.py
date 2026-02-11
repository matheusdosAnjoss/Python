from operator import itemgetter
dic = {}
lista = []

while True:
    dic['nome'] = str(input('Nome: '))
    dic['vitoria'] = int(input('Vitorias: '))
    dic['empate'] = int(input('Empates: '))
    dic['derrotas'] = int(input('Derrotas: '))
    dic['pontos'] = dic['vitoria'] * 3 + dic['empate']
    lista.append(dic.copy())

    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar: [S/N]')).upper()[0]

    if res == 'N':
        print('=='*20)
        break
    print('=='*20)

print('TABELA DE CLASSIFICAÇÂO')
print('=='*20)

rank = sorted(lista, key=itemgetter('pontos'), reverse=True)

for k, t in enumerate(rank):
    print(f'{k+1}º - {t['nome']}   =>  {t['pontos']} pontos.')
print('=='*20)