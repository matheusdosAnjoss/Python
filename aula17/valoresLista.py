ListaNum = list()

while True:
    n = (int(input('Digite um valor: ')))
    if n not in ListaNum:
        ListaNum.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('valor duplicado... Adicione outro número')

    continuar = ' ' 
    
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).upper().split()[0]
        if continuar in 'SN':
            break
        else:
            print('Digite S para sim e N para não...')
    
    if continuar == 'N':
        break
    
ListaNum.sort()
print(f'Você digitou os valores {ListaNum}')