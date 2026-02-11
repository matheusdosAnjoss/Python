ficha = []
dados = []
while True: 
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).upper().split()[0]
    if continuar == 'N':
        break

print('-='*20)
print('Nº   NOME           Média')
print('--'*20)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f} ')

while True:
    print('-='*20)
    opcao = int(input('Mostra nota de qual aluno? (999 interrompe): '))

    if opcao == 999:
        break

    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')

print('-='*20)