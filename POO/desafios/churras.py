from rich import print
from rich.panel import Panel

class churrasco:
    """
     Programa: Cálculo de Churrasco 🍖

    Este programa calcula a quantidade de carne necessária para um churrasco
    com base no número de convidados, considerando um consumo médio de
    0.400 kg de carne por pessoa e o preço fixo de R$ 82,40 por quilo.

    O sistema utiliza a biblioteca Rich para exibir as informações de forma
    organizada e visual no terminal, através de um painel (Panel).

    Autor: Matheus Oliveira
    """
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    #def conta(self):
        
    def analisar(self):
        #self.conta()
        self.kg_total = self.quant * 0.400
        self.ValorTotal = self.kg_total * 82.40
        self.ValorDividido = self.ValorTotal / self.quant

        caixa = Panel(f"Analisando [green]Churras dos Amigos[/] com [blue]{self.quant} convidados[/]\nCada participante comerá 0.400g e cada Kg custa R$82.40\nRecomendo [blue]comprar {self.kg_total:.3f}Kg[/] de carne\nO custo total será de [green]R${self.ValorTotal:.2f}[/]\nCada pessoa pagará [red]R${self.ValorDividido:.2f}[/] para participar.", title='Churras dos Amigos', expand=False)

        print(caixa)


c1 = churrasco(titulo='Churras dos Amigos', quant=15)
c1.analisar()  # 08:20