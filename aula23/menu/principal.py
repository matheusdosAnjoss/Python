import modulo01
import arquivo
from time import sleep

arq = 'cursoemVideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)


while True:
    resposta = modulo01.menu(['Ver pessoas cadastradas', 'Cadastrar novas Pessoas', 'Sair do Sistema'])
    
    if resposta == 1:
        #Opção de listar o conteudo de um arquivo!
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        modulo01.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = modulo01.leiaInt('idade: ')
        arquivo.cadastrar(arq, nome, idade)
        
    elif resposta == 3:
        modulo01.cabeçalho('Saindo do sistema até logo')
        break
    else:
        print('ERRO Digite uma opçao válida!')
    sleep(2)