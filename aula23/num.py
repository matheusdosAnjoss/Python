def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor, digite um número inteiro valido.\033[m')
            continue
        else:
            return n
        
def leiaFLoat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor, digite um número Real valido.\033[m')
            continue
        else:
            return n


n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFLoat('Digite um número Real: ')
print('--'*19)
print(f'Você acabou de digitar o número Interiro {n1}')
print(f'Você acabou de digitar um numero real {n2}')