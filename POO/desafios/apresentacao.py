def linha(tam=50):
    return '-'*tam

class funcionario:
    """
    Docstring para funcionario
    """

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def __str__(self):
        return f'Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor}'

print(linha())
c1 = funcionario(nome='Maria', setor='Administração', cargo='Diretora')
print(c1)

c2 = funcionario(nome='Pedro', setor='TI', cargo='Programador')
print(c2)
print(linha())