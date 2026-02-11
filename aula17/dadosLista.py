listaNum = []

while True:
    listaNum.append(int(input('Digite uma valor: ')))
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).upper().split()[0]
        if res in 'SN':
            break
        else:
            print('Digite S para sim e N para não')

    if res == 'N':
        break

print('-='*30)
listaNum.sort(reverse=True)
print(f'Você digitou {len(listaNum)} elementos.')
print(f'Os valores em ordem descrecente são {listaNum}')
if 5 not in listaNum:
    print('O valor 5 não foi encotrado na lista')
else:
    print('O valor 5 faz parte da lista')
print('-='*30)