# Declaração de Classe
class Gafanhoto:
    def __init__(self, nome = "", idade = 0): #Metodos Construtor
        # Atributos de Instancia
        self.nome = nome
        self.idade = idade

    #Metodo de Instancia
    def aniversario(self):
        self.idade += 1
    
    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"


# Declaração de Objetos

g1 = Gafanhoto(nome="matheus", idade=21)
g1.aniversario()
print(g1)
print(g1.__dict__)

g2 = Gafanhoto(nome='Melissa', idade= 12)
print(g2)



