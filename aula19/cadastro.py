cadastro = {}

cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = int(input('Ano de Nascimento: '))
cadastro['idade'] = 2025 - cadastro['idade']
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    
if cadastro['ctps'] != 0:
    cadastro['contraração'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Sálario: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] = ((cadastro['contraração'] + 35) - 2025 )

print('-='*20)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
print('-='*20)