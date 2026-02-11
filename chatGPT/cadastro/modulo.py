def linha(tam = 20):
    return '--' * tam

def ler_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um número inteiro!')
            continue
        else:
            return n
    
def ler_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Digite um número Real valido!')
            continue
        else:
            return n
    

def cadastroAlunos():
    print(linha())
    aluno = dict()
    aluno['nome'] = str(input('Nome do aluno: '))
    aluno['idade'] = ler_int('Idade: ')
    aluno['nota'] = ler_float('Nota: ')
    print(linha())
    return aluno

def mostra_relatorio(lista):
    print(linha())
    print(f'Total de alunos cadastrados: {len(lista)}')
    
    media = sum(a['nota'] for a in lista) / len(lista)
    print(f'Média das notas: {media:.2f}')

    melhor = max(lista, key=lambda x: x['nota'])
    print(f'Melhor aluno: {melhor['nome']} {melhor['nota']}')
    
    menores = []
    for a in lista:
        if a['idade'] < 18:
            menores.append(a['nome'])

        if len(menores) > 0:
            print(f'Alunos menores de 18 anos: ', menores)
        else:
            print(f'Nenhum aluno menor de idade')
    print(linha())
