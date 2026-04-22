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
        
        return frete
    

class Drone(Transporte):
    fator = 9.50

    def calc_frete(self):
        frete = self.distancia * self.fator
        if self.distancia > 10:
            return 'Raio maximo de 10Km'

        return frete
    
dist = 100
# entrega = Drone(dist)
# print(f'Frete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}')
opcoes = [Moto(dist) ,Carro(dist), Caminhao(dist), Drone(dist)]

# Criando a tabela do Rich
tabela = Table(show_header=True, header_style="bold magenta", expand=True)
tabela.add_column("Veículo", style="dim", width=12)
tabela.add_column("Distância", justify="right")
tabela.add_column("Custo do Frete", justify="right")

for t in opcoes:
    resultado = t.calc_frete()
    
    # Formatação visual: se for erro (string), fica vermelho. Se for valor, verde.
    if isinstance(resultado, str):
        valor_formatado = f"[red]{resultado}[/red]"
    else:
        valor_formatado = f"[green]R${resultado:.2f}[/green]"
    
    tabela.add_row(
        type(t).__name__, 
        f"{t.distancia} Km", 
        valor_formatado
    )

# Colocando a tabela dentro de um Painel
painel = Panel(
    tabela, 
    title="[bold]Calculadora de Logística[/bold]", 
    subtitle="Simulação de Frete",
    border_style="blue"
)

console = Console()
console.print(painel)