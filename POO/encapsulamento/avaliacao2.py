from rich import inspect

class Avaliacao:
    def __init__(self, nome, diciplina, nota=0):
        self.nome = nome
        self.diciplina = diciplina
        self._nota = nota #atributo protected

    # ATRIBUTO VALIDAVEL
    @property
    def nota(self): #GETTER
        return self._nota
    
    @nota.setter
    def nota(self, valor): #SETTER
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("ERRO")


av1 = Avaliacao('Ana', 'Matematica')
av1.nota = 69
print(f'{av1.nome} tirou {av1.nota} em {av1.diciplina}')
# inspect(av1, private=True)
