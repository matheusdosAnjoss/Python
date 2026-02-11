try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu não infomar os dados')
except Exception as erro:
    print(f'O eerp encontrado foi {erro.__cause__}')
else:
    print(r)