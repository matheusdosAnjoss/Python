dic = {}
lista = []
cont = 0
mulher = 0
while True:
    dic['nome'] = str(input('Nome: '))
    dic['sexo'] = ' '
    while dic['sexo'] not in 'MF':
        dic['sexo'] = str(input('Sexo: [M/F] ')).upper().split()[0]
        if dic['sexo'] in ['M', 'F']:
            break
        else:
            print('ERRO! Digite M pra masculino ou F pra feminino.')

    dic['idade'] = int(input('Idade: '))

    lista.append(dic.copy())
    cont += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? ')).upper().split()[0]
        if continuar in ['S', 'N']:
            break
        else:
            print('ERRO! Digite S para Sim e N para Não.')

    if continuar == 'N':
        break

somaIdade = 0
for p in lista:
    somaIdade += p['idade']
    
media = somaIdade / len(lista)

print('-='*25)
print(f'A) Ao todo temos {cont} pessoas cadastrada.')
print(f'B) Ao média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastrada foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p['nome']}',end= ' ')
print()

print('D) Pessoas com idade acima da média:')
for p in lista:
    if p['idade'] > media:
        print(f'   Nome = {p['nome']}, sexo = {p['sexo']}, idade = {p['idade']}')
print('<<ENCERRADO>>')
print('-='*25)
