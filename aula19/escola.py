lista = {}

while True:
    print('-='* 25)
    lista['nome'] = str(input('Nome: '))
    lista['media'] = float(input(f'Média de {lista['nome']}: '))
    print('-='* 25)

    for k, v in lista.items():
        print(f'{k} é igual a {v}')

    if lista['media'] >= 7:
        print(f'Situaçao é igual a Aprovado')
    elif 5 <= lista['media'] < 7:
        print(f'Situação é igual a Recuperção')
    else:
        print(f'Situação é igual a Reprovado')
    print('-='* 25)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).upper().split()[0]

    if continuar == 'N':
        break

print('Programa encerrado...')