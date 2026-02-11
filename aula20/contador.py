from time import sleep
print('--'*20)
def cont1():
    i = 1
    f = 10
    p = 1
    print(f'Contagem de {i} até {f} em {p}')
    for c in range(i,f+1,p):
        print(f'{c}', end=' ', flush=True)
        sleep(0.3)

def cont2():
    i = 10
    f = 0
    p = 2
    print(f'Contagem de {i} até {f} em {p}')
    for c in range(i,f-1,-p):
        print(f'{c}', end=' ', flush=True)
        sleep(0.3)
        
def contador(i,f,p):
    print(f'Contagem de {i} até {f} em {p}')
    if i > f:
        for c in range(i,f-1,-p):
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
        print('FIM')
    else:
        for c in range(i,f+1,p):
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
        print('FIM')

cont1()

print()
print('--'*20)

cont2()

print()
print('--'*20)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('--'*20)
contador(inicio,fim,passo)