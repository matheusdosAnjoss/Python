palavras = ('aprender', 'programa', 'linguagem', 'python', 'curso', 'estudar', 'matheus')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')