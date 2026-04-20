from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    """
    Classe abstrata que serve como base para todos os polígonos e formas.
    
    Define a interface obrigatória para o cálculo de propriedades 
    geométricas básicas.
    """
    def __init__(self, qtd_lados= 0):
        self.qtd_lados = qtd_lados
    
    @abstractmethod
    def perimetro(self):
        """Calcula o comprimento total do contorno da forma."""
        pass

    @abstractmethod
    def area(self):
        """Calcula a superfície total ocupada pela forma."""
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        self.lado = lado
    
    def perimetro(self):
        return self.lado * 4
    
    def area(self):
        return self.lado ** 2
    

class Circulo(Poligono):
    def __init__(self,  raio):
        self.raio = raio

    def perimetro(self):
        return 2 * pi * self.raio
    
    def area(self):
        return pi * (self.raio ** 2)
    

# p1 = Circulo(20)
# print(f'Perimetro = {p1.perimetro():.1f}')
# print(f'Area = {p1.area():.1f}')

formas = [Quadrado(5), Circulo(3)]

print("-" * 20)
for forma in formas:
    print(f"Forma: {type(forma).__name__}")
    print(f"Área: {forma.area():.2f}")
    print(f"Perímetro: {forma.perimetro():.2f}")
    print("-" * 20)