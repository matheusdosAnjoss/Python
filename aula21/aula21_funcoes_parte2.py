
# ===============================================
# CURSO EM VÍDEO - PYTHON - AULA 21
# FUNÇÕES (PARTE 2) - Prof. Gustavo Guanabara
# ===============================================

# Exemplo 1: Função com Docstring
def contador(i, f, p):
    """ 
    Faz uma contagem de i até f de p em p.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


# Exemplo 2: Usando help() para ver a docstring
# help(contador)


# Exemplo 3: Função com parâmetros opcionais
def soma(a=0, b=0, c=0):
    """ 
    Soma até três valores e mostra o resultado.
    :param a: primeiro valor (padrão 0)
    :param b: segundo valor (padrão 0)
    :param c: terceiro valor (padrão 0)
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')


# Exemplo 4: Função com retorno
def fatorial(n=1):
    """
    Calcula o fatorial de n.
    :param n: número inteiro para calcular o fatorial
    :return: o valor do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


# Exemplo 5: Função com retorno + uso prático
def par(n=0):
    """
    Verifica se um número é par.
    :param n: número a ser testado
    :return: True se for par, False se for ímpar
    """
    return n % 2 == 0


# ==================== TESTES =====================
print('-' * 40)
print('Testando contador():')
contador(1, 10, 2)

print('\n' + '-' * 40)
print('Testando soma():')
soma(3, 2, 5)
soma(8, 4)
soma()

print('\n' + '-' * 40)
print('Testando fatorial():')
print(f'O fatorial de 5 é {fatorial(5)}')
print(f'O fatorial de 4 é {fatorial(4)}')
print(f'O fatorial de 1 é {fatorial()}')

print('\n' + '-' * 40)
print('Testando par():')
num = 7
print(f'O número {num} é par? {par(num)}')
num = 8
print(f'O número {num} é par? {par(num)}')
