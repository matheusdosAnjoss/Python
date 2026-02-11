# Declaração de Classe
class Gafanhoto:
    def __init__(self): #Metodos Construtor
        # Atributos de Instancia
        self.nome = ""
        self.idade = 0

    #Metodo de Instancia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"


# Declaração de Objetos

g1 = Gafanhoto()
g1.nome = 'Matheus'
g1.idade = 21
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Melissa"
g2.idade = 12
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = 'Jocimara'
g3.idade = 43
print(g3.mensagem())