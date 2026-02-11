def leiaInt(msg):
    ok = False
    Valor = 0

    while True:
        n = str(input(msg))
        if n.isnumeric():
            Valor = int(n)
            ok = True
            return n
            break
        else:
            print('ERRO Digite um número válido')


n = leiaInt('Digite um numero:')
print(f'Você acabou de digitar o número {n}')