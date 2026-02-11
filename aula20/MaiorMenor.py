from random import randint
def Maior (*val):
    print('=='*22)
    print('Analisando os valores passados...')
    maiorN = max(val)
    
    for v in val:
        print(f'{v}', end=' ')

    print(f'Foram infomados {len(val)} valores ao todo.')
    print(f'O Maior valor informado foi {maiorN}')
  
Maior(2,9,4,5,7,1)
Maior(4,7,0)
Maior(1,2)
Maior(6)
Maior(0)
print('=='*22)