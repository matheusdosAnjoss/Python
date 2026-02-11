def mensagem(msg):
    print('--'*10)
    print(msg)
    print('--'*10)

def minha_fucao(num1=0,num2=0):
    res = num1+num2
    print(res)


mensagem(f' SISTEMA DE SOMA')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
minha_fucao(n1,n2)


