
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    
    if num < 0:
        break
    print('='*30)
    
    cont = 0
    while cont <= 9:
        cont += 1
        res = num*cont
        print(f'{num} x {cont} = {res}')
    print('='*30)

print('PROGRAMA ENCERRADO...')