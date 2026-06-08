from rich import inspect

class Avaliacao:
    def __init__(self, nome, diciplina, nota=0):
        self.nome = nome
        self.diciplina = diciplina
        self._nota = nota

    def get_nota(self):
        return self._nota

    def set_nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("ERRO")
    

av1 = Avaliacao('Ana', 'Matematica')
av1.set_nota(90)
print(f'{av1.nome} tirou {av1.get_nota()} em {av1.diciplina}')
# inspect(av1, private=True)
