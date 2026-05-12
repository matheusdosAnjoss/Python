from abc import ABC, abstractmethod
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def calc_frete(self):
        frete = self.distancia * self.fator
        return frete
    

class Carro(Transporte):
    fator = 0.90

    def calc_frete(self):
        frete = self.distancia * self.fator
        return frete

class Caminhao(Transporte):
    fator = 1.20

    def calc_frete(self):
        frete = self.distancia * self.fator
        if self.distancia < 50:
            return 'Raio minimo de 50Km'
        
        return f"{frete:.2f}"
    

class Drone(Transporte):
    fator = 9.50

    def calc_frete(self):
        frete = self.distancia * self.fator
        if self.distancia > 10:
            return 'Raio maximo de 10Km'

        return frete

dist = 100

opcoes = [Moto(dist), Carro(dist), Caminhao(dist), Drone(dist)]


tabela = Table(title="Tabela de fretes", show_header=True, header_style= "bold blue", expand=True )

tabela.add_column("Tipo")
tabela.add_column('Distancia')
tabela.add_column('Frete')

for item in opcoes:
    tabela.add_row(
        type(item).__name__,
        f"{dist} Km",
        f"{item.calc_frete()}"
    )


console = Console()
console.print(tabela)