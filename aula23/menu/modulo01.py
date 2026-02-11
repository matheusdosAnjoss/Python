def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor, digite um número inteiro valido.\033[m')
            continue
        else:
            return n

def linha(tam = 20):
    return '--' * tam

def cabeçalho(msg):
    print(linha())
    print(msg.center(40))
    print(linha())
    
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1

    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc




