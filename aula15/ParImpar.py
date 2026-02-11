from random import randint
v = 0
while True:
    jogador = int(input('Diga um número: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar [P/I]: ')).upper()[0]
    
    print(f'Você jogou {jogador} é o computador jogou {computador}, é o Total de {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VECEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('VoCÊ VECEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente? ')
print(f'Gamer over! Você venceu {v} vezes')
    
