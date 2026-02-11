dados = {}
dados['nome'] = str(input('Nome: '))
dados['idade'] = int(input('Idade: '))
dados['sexo'] = str(input('sexo: '))

for k, v in dados.items():
    print(f'{k}: {v}')