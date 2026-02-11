sexo = str(input('Informe o Sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'M' 'F':
    sexo = str(input('Dados invalidos, por favor informe seu sexo: ')).strip().upper()[0]

if sexo == 'M':
    print('Seu sexo é Masculino')
elif sexo == 'F':
    print('Seu sexo é Feminino')
