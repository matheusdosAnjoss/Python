from rich import print
from rich.panel import Panel

class produto:
    """
    EMITE UMA ETIQUETA MOSTRANDO O NOME E O PREÇO DO PRODUTO        
    """
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        self.precof = f"Preço: R${self.preco:.2f}"

        caixa = Panel(f"{self.nome.center(29, ' ')}  {self.precof.center(30, '-')}", title='Produto', width=35)
        print(caixa)
        
    
p1 = produto(nome='Iphone 17 pro Max', preco=7200)
p2 = produto(nome='Xbox Series S', preco=2500)
p3 = produto(nome='Notebook Gamer', preco=5000)

p1.etiqueta()
p2.etiqueta()
p3.etiqueta()

