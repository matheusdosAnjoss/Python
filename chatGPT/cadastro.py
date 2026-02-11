dicionario = {}
lista = []
cont = 0
while True:
    dicionario['nome'] = str(input('Nome: '))
    dicionario['idade'] = int(input('Idade: '))
    dicionario['cargo'] = str(input('Cargo: '))
    dicionario['salario'] = float(input('Salário: '))
    lista.append(dicionario.copy())
    cont += 1
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).upper()[0]

    if res == 'N':
        break
    
print('=='*25)
print(f'Foram cadastrados {cont} fucionarios.')

somaSalario = 0
for s in lista:
    somaSalario += s['salario']
media = somaSalario / len(lista)

print(f'A média dos salario é R${media:.2f}')
print(f'Fucionários com sálario acima da média:', end=' ')
for n in lista:
    if n['salario'] >= media:
        print(f'{n['nome']}', end=' ')