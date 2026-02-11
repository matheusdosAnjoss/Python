galera = []
dados = []
totMaior = totMenor = 0
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
    
print('-='*30)
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totMaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totMenor += 1

print(f'Temos {totMaior} de maiores de idade e {totMenor} menor de idade')
print('-='*30)