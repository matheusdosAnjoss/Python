def verificarIdade(n, i):
    if i < 18:
        return f"{n} tem {i} anos e é Menor de idade."
    else:
        return f"{n} tem {i} anos e é Maior de idade."

nome = str(input('Nome: '))
idade = int(input('idade: '))

print(verificarIdade(nome, idade))