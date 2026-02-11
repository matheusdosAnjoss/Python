def linha(tam = 25):
    print('-' * tam)

def ler_nome(msg):
    linha()
    while True:
        n = input(msg).strip()
        if n == "":
            print('Digite seu nome para proseguir!')
            continue
        else:
            return n
        
def ler_idade(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 0:
                print('Idade não pode ser negativa!')
                continue
        except (ValueError, TypeError):
            print('Digite sua idade!')
            continue
        else:
            return n
        
def deseja_continuar(msg="Quer cadastrar outra pessoa? [S/N] "):
    while True:
        linha()
        resp = ' '
        while resp not in 'SN':
            resp = input(msg).strip().upper()[0]
            if resp not in 'S' 'N':
                print("\033[31mResposta inválida! Digite apenas S ou N.\033[m")
                continue
        return resp
    
def cadastros():
    pessoas = dict()
    pessoas['nome'] = ler_nome('Nome: ')
    pessoas['idade'] = ler_idade('Idade: ')
    return pessoas

def mostrar_cadastro(lista):
    #for p in lista:
        #print(f'Nome: {p['nome']} Idade: {p['idade']} ')
    linha()
    for p in lista:
        if p['idade'] < 18:
            print(f'Nome: {p['nome']}\nIdade: {p['idade']}\nmenor de idade ')
        else:
            print(f'Nome: {p['nome']} Idade: {p['idade']} é maior de idade ')
    linha()



cadastro = list()

while True:
    cadastro.append(cadastros())
    #nome = ler_nome('Nome: ')
    #idade = ler_idade('Idade: ')
    linha()
    print('Cadastro realizado')
    linha
    #print(f'Nome: {nome}')
    #print(f'Idade: {idade}')

    #if idade < 18:
    #    print('Menor de idade')

    #else:
    #    print('Maior de idade')

    if deseja_continuar() == 'N':
        mostrar_cadastro(cadastro)
        break