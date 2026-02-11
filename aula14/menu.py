n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

opcao = 0

while opcao != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')

    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print('='*50)
        print(f'A soma entre o número {n1} e {n2} é igual a {soma}')
        print('='*50)
    elif opcao == 2:
        soma = n1 * n2
        print('='*50)
        print(f'A multiplicação entre o número {n1} e {n2} é igual a {soma}')
        print('='*50)
    elif opcao == 3:
        maior = max(n1,n2)
        print('='*30)
        print(f'O maior número é {maior}')
        print('='*30)
    elif opcao == 4:
        print('='*50)
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
        print('='*50)
    elif opcao == 5:
        print('='*30)
        print('Programa Finalizado!')
        print('='*30)
    else:
        print('='*35)
        print('Opção invalida... Tente novamente!')
        print('='*35)