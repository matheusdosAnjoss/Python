class Mae():
    def __init__(self, nome:str = "Mamãe"):
        self.nome = nome

    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com leite condensado e calda')

    def fritar_coxinha(self):
        print(f'{self.nome} frita coxinha no oleo de soja')


class Filha(Mae):
    def fritar_coxinha(self):
        print(f'{self.nome} frita coxinha na Air Flyer')

class Filho(Mae):
    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com leite ninho com nutela')
    

p1 = Mae('Maria')
p2 = Filho('Matheus')
p3 = Filha('Melissa')

p1.fritar_coxinha()
p1.fazer_pudim()

print()

p2.fritar_coxinha()
p2.fazer_pudim()

print()

p3.fritar_coxinha()
p3.fazer_pudim()