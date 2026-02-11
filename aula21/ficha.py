# Função chamada 'ficha' que mostra o nome do jogador e quantos gols ele fez

def ficha(n='<desconhecido>', g=0): 
    # Mostra a mensagem com o nome e os gols
    return print(f'O jogador {n} fez {g} gols')
    
    
nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols? '))

print('==' * 20)

# Verifica se a pessoa digitou um número em 'gols'
if gols.isnumeric():  
    gols = int(gols) # Se for número, transforma de texto (str) para número (int)
else:
    gols = 0 # Se não for número, ou se deixar em branco, define gols como 0

# Verifica se o nome ficou em branco (sem digitar nada)
if nome.strip() == '': # Se o nome estiver em branco, chama a função só com os gols
    # (o nome vai ser '<desconhecido>')
    ficha(g=gols)
else:
    ficha(nome, gols) # Se o nome tiver algo escrito, chama a função normalmente
