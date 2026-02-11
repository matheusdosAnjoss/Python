import modulo

alunos = list()

while True:
    alunos.append(modulo.cadastroAlunos())
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar: [S/N]')).upper().split()[0]
    
    if res == 'N':
        break

modulo.mostra_relatorio(alunos)