MaiorIdade = 0
homen = mulher = 0
while True:
    print('-'*25)
    print('CADASTRO DE PESSOAS')
    print('-'*25)
    
    idade = int(input('Idade: '))
    if idade >= 18:
        MaiorIdade += 1

    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).upper().split()[0]
        if sexo in ['M','F']:
            break
        else:
            print('Digite M para Masculino e F para Feminino: ')
    
    if sexo == 'M':
        homen += 1
    elif sexo == 'F':
        if idade <= 20:
            mulher += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).upper().split()[0]
        if continuar in ['S','N']:
            break
        else:
            print('Digite S para Sim e N para Não...')
    
    if continuar == 'N':
        break

print('-'*35)
print(f'Temos {MaiorIdade} pessoas maiores de 18 anos')
print(f'Ao todo Temos {homen} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')
print('-'*35)
print('FIM')