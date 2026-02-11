contIdade = 0
homem = mulher = 0
while True:
    print('-'*22)
    print('CADASTRE UMA PESSOA')
    print('-'*22)
    
    idade = int(input('Idade: '))
    if idade >= 18:
        contIdade += 1

    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).upper().split()[0]
        if sexo in ['M', 'F']:
            break
        else:
            print('Digite apenas M (masculino) ou F (feminino).')

    if sexo == 'M':
        homem += 1
    elif sexo == 'F':
        if idade < 20:
            mulher += 1
         
    sn = ' '
    print('-'*22)
    while sn not in 'SsNn':
        sn = str(input("Quer continuar? [S/N] ")).upper().split()[0]
        if sn in ['S', 'N']:
            break
        else:
            print('Digite apenas S (sim) ou N (não).')
    
    if sn == 'N':
        print('FIM')
        break
    
print('-'*35)
print(f'Total de pessoas com mais de 18 anos: {contIdade}')
print(f'Ao todo temos {homem} homens cadastrado')
print(f'E temos {mulher} mulheres com menos de 20 anos')
print('FIM DO PROGRAMA..')
print('-'*35)
