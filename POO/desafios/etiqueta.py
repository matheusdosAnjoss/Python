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
        caixa = Panel(f"{self.nome}\nPreço: R${self.preco:.2f}", title='Produto', width=30)
        print(caixa)
        
    
p1 = produto(nome='Iphone', preco=1200)
p2 = produto(nome='Xbox Series S', preco=2500)

p1.etiqueta()
p2.etiqueta()

