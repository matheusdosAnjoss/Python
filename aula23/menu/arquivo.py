import modulo01

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False #Se o Python não encontrar o arquivo → retorna False.
    else:
        return True #se abriu sem erro o arq existe
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        modulo01.cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')

    finally: #DANDO CERTO OU ERRADO VAI FECHAR O ARQUIVO
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um erro na arbertura do arquivo!")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()